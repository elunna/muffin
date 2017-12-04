#!/usr/bin/env python
"""
Main entry point.
"""
import argparse
from src import logger


def setup_parser():
    # Setup argparser
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', help='Increase output verbosity.', action="store_true")
    return parser


if __name__ == "__main__":
    args = parser.parse_args()
	log = logger.setup_logger()
    log.debug('Hello Equestria!')
    
    if args.verbose:
		log.debug('Verbose enabled!')
