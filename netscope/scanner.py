import socket
from concurrent.futures import ThreadPoolExecutor
import time
from netscope.models import ScanResult

def scan_port(host: str, port: int, timeout: float = 1.0) -> ScanResult:
    """Check whether a TCP port accepts a connection."""

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)

        start = time.perf_counter()

        try:
            sock.connect((host, port))
            latency_ms = (time.perf_counter() - start) * 1000

            return ScanResult(
                port=port,
                is_open=True,
                latency_ms=latency_ms,
            )

        except (socket.timeout, ConnectionRefusedError, OSError):
            return ScanResult(
                port=port,
                is_open=False,
            )

def parse_port_range(port_range: str) -> list[int]:
    """Convert a port range string into a list of valid TCP ports."""

    start, end = map(int, port_range.split("-"))

    if not (1 <= start <= 65535):
        raise ValueError("Start port must be between 1 and 65535.")

    if not (1 <= end <= 65535):
        raise ValueError("End port must be between 1 and 65535.")

    if start > end:
        raise ValueError("Start port cannot be greater than end port.")

    return list(range(start, end + 1))


def scan_ports(
    host: str,
    ports: list[int],
    timeout: float = 1.0,
    workers: int = 50,
) -> list[ScanResult]:
    """Scan multiple TCP ports concurrently."""

    with ThreadPoolExecutor(max_workers=workers) as executor:
        results = executor.map(
            lambda port: scan_port(host, port, timeout),
            ports,
        )

        return list(results)
