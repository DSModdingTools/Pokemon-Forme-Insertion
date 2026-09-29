import argparse

import my_constants


def get_parsed_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        add_help=True,
        allow_abbrev=False,
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {my_constants.version}"
    )
    parser.add_argument(
        "-v", "--verbose", help="increase output verbosity", action="store_true"
    )
    parser.add_argument(
        "--logserver", dest="log_server_port", type=int, metavar="{1..65535}"
    )
    args = parser.parse_args()
    return args
