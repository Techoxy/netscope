from netscope.scanner import scan_port, scan_ports


def test_closed_port():
    assert scan_port("127.0.0.1", 1) is False


def test_scan_ports():
    assert scan_ports("127.0.0.1", [1, 2, 3]) == []
