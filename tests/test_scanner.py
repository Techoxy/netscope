from netscope.scanner import scan_port, scan_ports
from netscope.scanner import parse_port_range, scan_port, scan_ports

def test_parse_port_range():
    assert parse_port_range("80-85") == [80, 81, 82, 83, 84, 85]


def test_single_port_range():
    assert parse_port_range("443-443") == [443]


def test_invalid_port_range():
    try:
        parse_port_range("70000-70005")
        assert False
    except ValueError:
        assert True

def test_closed_port():
    assert scan_port("127.0.0.1", 1) is False


def test_scan_ports():
    assert scan_ports("127.0.0.1", [1, 2, 3]) == []
