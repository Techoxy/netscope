from dataclasses import dataclass


@dataclass
class ScanResult:
    """Result of a TCP port scan."""

    port: int
    is_open: bool
    latency_ms: float | None = None
