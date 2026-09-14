from netscope.engine import run_scan


def test_run_scan_closed_ports():
    results = run_scan("127.0.0.1", [1, 2, 3])

    assert len(results) == 3
    assert all(result.is_open is False for result in results)
    assert all(result.service_info is None for result in results)
