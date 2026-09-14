from netscope.analyzer import analyze_service
from netscope.resolver import resolve_target
from netscope.scanner import scan_ports


def run_scan(
    host: str,
    ports: list[int],
    timeout: float = 1.0,
    workers: int = 50,
):
    """Run a TCP scan and analyze discovered open services."""

    target_ip = resolve_target(host)

    results = scan_ports(
        host=target_ip,
        ports=ports,
        timeout=timeout,
        workers=workers,
    )

    for result in results:
        if result.is_open:
            result.service_info = analyze_service(
                target_ip,
                result.port,
            )

    return results
