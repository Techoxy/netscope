from netscope.models import ScanResult, ServiceInfo
from netscope.output import format_terminal


def test_format_terminal():
    results = [
        ScanResult(
            port=9001,
            is_open=True,
            latency_ms=0.25,
            service_info=ServiceInfo(
                service="HTTP",
                version="TestServer/1.0",
            ),
        ),
        ScanResult(
            port=9002,
            is_open=False,
        ),
    ]

    output = format_terminal(results)

    assert "9001" in output
    assert "OPEN" in output
    assert "HTTP" in output
    assert "9002" not in output
