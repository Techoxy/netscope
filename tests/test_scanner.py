from netscope.scanner import scan_port


def test_closed_port():
    assert scan_port("127.0.0.1", 1) is False
