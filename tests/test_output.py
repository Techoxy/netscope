import json

from netscope.models import ScanResult, ServiceInfo
from netscope.output import format_json, format_terminal


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

    assert "PORT" in output
    assert "STATE" in output
    assert "9001" in output
    assert "OPEN" in output
    assert "HTTP" in output
    assert "TestServer/1.0" in output
    assert "Ports scanned: 2" in output
    assert "Open ports:   1" in output
    assert "Closed ports: 1" in output


def test_format_terminal_unknown_service():
    results = [
        ScanResult(
            port=9003,
            is_open=True,
            latency_ms=0.50,
        )
    ]

    output = format_terminal(results)

    assert "9003" in output
    assert "unknown" in output


def test_format_json():
    results = [
        ScanResult(
            port=9001,
            is_open=True,
            latency_ms=0.25,
            service_info=ServiceInfo(
                service="HTTP",
                version="TestServer/1.0",
            ),
        )
    ]

    output = format_json(results)
    data = json.loads(output)

    assert data[0]["port"] == 9001
    assert data[0]["is_open"] is True
    assert data[0]["service"] == "HTTP"
    assert data[0]["version"] == "TestServer/1.0"
