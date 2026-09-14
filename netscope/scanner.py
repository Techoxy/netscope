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
) -> list[int]:
    """Scan multiple TCP ports and return the ports that are open."""

    open_ports = []

    for port in ports:
        if scan_port(host, port, timeout):
            open_ports.append(port)

    return open_ports
