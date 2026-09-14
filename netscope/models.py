from dataclasses import dataclass


@dataclass
class ServiceInfo:
    """Information identified about a network service."""

    service: str
    version: str | None = None
    banner: str | None = None


@dataclass
class ScanResult:
    """Result of a TCP port scan."""

    port: int
    is_open: bool
    latency_ms: float | None = None
    service_info: ServiceInfo | None = None
