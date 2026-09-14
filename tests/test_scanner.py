from netscope.scanner import parse_port_range, scan_port, scan_ports


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


def test_invalid_port_range():
    try:
        parse_port_range("70000-70005")
        assert False
    except ValueError:
        assert True
