import argparse
from netscope.output import format_json,format_terminal
from netscope.engine import run_scan
from netscope.scanner import parse_port_range


def build_parser() -> argparse.ArgumentParser:
    """Build the NetScope command-line argument parser."""

    parser = argparse.ArgumentParser(
        prog="netscope",
        description="Network reconnaissance and TCP service analysis tool.",
    )

    parser.add_argument(
        "target",
        help="Target host or IP address.",
    )

    parser.add_argument(
        "--ports",
        default="1-1024",
        help="TCP port range to scan (default: 1-1024).",
    )

    parser.add_argument(
        "--timeout",
        type=float,
        default=1.0,
        help="Connection timeout in seconds (default: 1.0).",
    )

    parser.add_argument(
        "--workers",
        type=int,
        default=50,
        help="Maximum concurrent workers (default: 50).",
    )

    parser.add_argument(
        "--format",
        choices=["terminal", "json"],
        default="terminal",
        help="Output format (default: terminal).",
    )
    return parser


def main() -> None:
    """Run the NetScope command-line interface."""

    parser = build_parser()
    args = parser.parse_args()

    try:
        ports = parse_port_range(args.ports)

        if args.timeout <= 0:
            raise ValueError("Timeout must be greater than 0.")

        if args.workers <= 0:
            raise ValueError("Workers must be greater than 0.")

        results = run_scan(
            host=args.target,
            ports=ports,
            timeout=args.timeout,
            workers=args.workers,
        )

    except ValueError as exc:
        parser.error(str(exc))

    if args.format == "json":
       print(format_json(results))
    else:
       print(format_terminal(results))

if __name__ == "__main__":
    main()
