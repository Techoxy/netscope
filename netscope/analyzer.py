import socket
from collections.abc import Callable

from netscope.models import ServiceInfo


def grab_banner(
    host: str,
    port: int,
    timeout: float = 2.0,
) -> str | None:
    """Attempt to retrieve a passive service banner."""

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)

        try:
            sock.connect((host, port))

            data = sock.recv(1024)

            if not data:
                return None

            return data.decode("utf-8", errors="replace").strip()

        except (socket.timeout, ConnectionRefusedError, OSError):
            return None


def probe_http(
    host: str,
    port: int,
    timeout: float = 2.0,
) -> str | None:
    """Send a minimal HTTP request and return the response headers."""

    request = (
        f"HEAD / HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        f"Connection: close\r\n"
        f"\r\n"
    )

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)

        try:
            sock.connect((host, port))
            sock.sendall(request.encode("ascii"))

            data = sock.recv(4096)

            if not data:
                return None

            return data.decode("utf-8", errors="replace").strip()

        except (socket.timeout, ConnectionRefusedError, OSError):
            return None


def identify_http(response: str) -> ServiceInfo | None:
    """Identify HTTP service information from an HTTP response."""

    lines = response.splitlines()

    if not lines:
        return None

    if not lines[0].startswith("HTTP/"):
        return None

    server_header = None

    for line in lines[1:]:
        if line.lower().startswith("server:"):
            server_header = line.split(":", 1)[1].strip()
            break

    return ServiceInfo(
        service="HTTP",
        version=server_header,
        banner=response,
    )


def identify_ssh(response: str) -> ServiceInfo | None:
    """Identify SSH service information from an SSH banner."""

    if not response.startswith("SSH-"):
        return None

    parts = response.split("-", 2)

    if len(parts) < 3:
        return None

    return ServiceInfo(
        service="SSH",
        version=parts[1],
        banner=response,
    )


Detector = Callable[[str], ServiceInfo | None]

DETECTORS: tuple[Detector, ...] = (
    identify_http,
    identify_ssh,
)


def identify_service(response: str) -> ServiceInfo | None:
    """Identify a service using the registered protocol detectors."""

    for detector in DETECTORS:
        info = detector(response)

        if info:
            return info

    return None


def analyze_service(
    host: str,
    port: int,
) -> ServiceInfo | None:
    """Attempt to identify the service running on a port."""

    response = probe_http(host, port)

    if response:
        info = identify_service(response)

        if info:
            return info

    response = grab_banner(host, port)

    if response:
        return identify_service(response)

    return None
