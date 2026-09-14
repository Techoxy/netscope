from netscope.models import ScanResult


def format_terminal(results: list[ScanResult]) -> str:
    """Format scan results for human-readable terminal output."""

    lines = []

    for result in results:
        if not result.is_open:
            continue

        service = (
            result.service_info.service
            if result.service_info
            else "unknown"
        )

        latency = (
            f"{result.latency_ms:.2f} ms"
            if result.latency_ms is not None
            else "-"
        )

        lines.append(
            f"{result.port:5}  OPEN  "
            f"{latency:>10}  {service}"
        )

    return "\n".join(lines)
