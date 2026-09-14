import socket


def resolve_target(target: str) -> str:
    """Resolve a hostname or IP address to an IPv4 address."""

    try:
        return socket.gethostbyname(target)
    except socket.gaierror as exc:
        raise ValueError(f"Unable to resolve target: {target}") from exc
