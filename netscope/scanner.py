import socket


def scan_port(host: str, port: int, timeout: float = 1.0) -> bool:
    """Check whether a TCP port accepts a connection."""

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)

        try:
            sock.connect((host, port))
            return True
        except (socket.timeout, ConnectionRefusedError, OSError):
            return False


def scan_ports(
    host: str,
    ports: list[int],
    timeout: float = 1.0,
) -> list[int]:
    """Scan multiple TCP ports and return the ports that are open."""

    open_ports = []

    for port in ports:
        if scan_port(host, port, timeout):
            open_ports.append(port)

    return open_ports
