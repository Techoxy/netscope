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
