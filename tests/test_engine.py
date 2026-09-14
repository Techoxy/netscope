from unittest.mock import patch

from netscope.engine import run_scan


def test_run_scan():
    with patch("netscope.engine.resolve_target", return_value="127.0.0.1"):
        results = run_scan(
            host="localhost",
            ports=[80],
        )

    assert len(results) == 1
    assert results[0].port == 80


def test_run_scan_resolves_target():
    with patch("netscope.engine.resolve_target", return_value="127.0.0.1") as mock_resolve:
        run_scan(
            host="localhost",
            ports=[80],
        )

    mock_resolve.assert_called_once_with("localhost")
