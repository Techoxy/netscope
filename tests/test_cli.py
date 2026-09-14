import pytest

from netscope.cli import build_parser, main


def test_default_arguments():
    parser = build_parser()

    args = parser.parse_args(["127.0.0.1"])

    assert args.target == "127.0.0.1"
    assert args.ports == "1-1024"
    assert args.timeout == 1.0
    assert args.workers == 50


def test_custom_arguments():
    parser = build_parser()

    args = parser.parse_args(
        [
            "127.0.0.1",
            "--ports",
            "80-443",
            "--timeout",
            "0.5",
            "--workers",
            "10",
        ]
    )

    assert args.target == "127.0.0.1"
    assert args.ports == "80-443"
    assert args.timeout == 0.5
    assert args.workers == 10


@pytest.mark.parametrize("timeout", ["0", "-1"])
def test_invalid_timeout(timeout, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["netscope", "127.0.0.1", "--timeout", timeout],
    )

    with pytest.raises(SystemExit):
        main()


@pytest.mark.parametrize("workers", ["0", "-1"])
def test_invalid_workers(workers, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["netscope", "127.0.0.1", "--workers", workers],
    )

    with pytest.raises(SystemExit):
        main()
