#!/usr/bin/env python
"""
Main entry point.
"""
import argparse
from src import logger


def main():
    log = logger.setup_logger()
    log.debug('Hello Equestria! From src!')


if __name__ == "__main__":
    # Setup argparser
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', help='increase output verbosity', action="store_true")
    args = parser.parse_args()

    if args.verbose:
        main()
