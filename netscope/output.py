import json

from netscope.models import ScanResult


def format_terminal(results: list[ScanResult]) -> str:
    """Format scan results as a human-readable terminal report."""

    lines = [
        "PORT   STATE   LATENCY      SERVICE   VERSION",
        "-" * 50,
    ]

    open_count = 0

    for result in results:
        if not result.is_open:
            continue

        open_count += 1

        service = (
            result.service_info.service
            if result.service_info
            else "unknown"
        )

        version = (
            result.service_info.version
            if result.service_info and result.service_info.version
            else "-"
        )

        latency = (
            f"{result.latency_ms:.2f} ms"
            if result.latency_ms is not None
            else "-"
        )

        lines.append(
            f"{result.port:<6}"
            f"{'OPEN':<8}"
            f"{latency:<13}"
            f"{service:<10}"
            f"{version}"
        )

    lines.extend(
        [
            "",
            f"Ports scanned: {len(results)}",
            f"Open ports:   {open_count}",
            f"Closed ports: {len(results) - open_count}",
        ]
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
