import pytest

from netscope.cli import build_parser


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
