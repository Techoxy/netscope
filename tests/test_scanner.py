from netscope.scanner import parse_port_range, scan_port, scan_ports
import pytest


def test_closed_port():
    result = scan_port("127.0.0.1", 1)

    assert result.port == 1
    assert result.is_open is False
    assert result.latency_ms is None


def test_scan_ports():
    results = scan_ports("127.0.0.1", [1, 2, 3])

    assert len(results) == 3
    assert all(result.is_open is False for result in results)


def test_parse_port_range():
    assert parse_port_range("80-85") == [80, 81, 82, 83, 84, 85]


def test_single_port_range():
    assert parse_port_range("443-443") == [443]

def test_single_port():
    assert parse_port_range("443") == [443]


def test_multiple_ports():
    assert parse_port_range("22,80,443") == [22, 80, 443]


def test_mixed_port_specification():
    assert parse_port_range("20-22,80,443") == [20, 21, 22, 80, 443]


def test_duplicate_ports():
    assert parse_port_range("80,80,81") == [80, 81]


def test_invalid_port_range():
    try:
        parse_port_range("70000-70005")
        assert False
    except ValueError:
        assert True
def test_invalid_single_port():
    try:
        parse_port_range("70000")
        assert False
    except ValueError:
        assert True


def test_invalid_port_specification():
    try:
        parse_port_range("80-90-100")
        assert False
    except ValueError:
        assert True
def test_invalid_single_port_format():
    with pytest.raises(ValueError, match="Invalid port: abc"):
        parse_port_range("abc")


def test_invalid_port_range_format():
    with pytest.raises(ValueError, match="Invalid port range: 80-"):
        parse_port_range("80-")
