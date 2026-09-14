import json

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


def format_json(results: list[ScanResult]) -> str:
    """Format scan results as JSON."""

    data = []

    for result in results:
        item = {
            "port": result.port,
            "is_open": result.is_open,
            "latency_ms": result.latency_ms,
            "service": None,
            "version": None,
        }

        if result.service_info:
            item["service"] = result.service_info.service
            item["version"] = result.service_info.version

        data.append(item)

    return json.dumps(data, indent=2)
