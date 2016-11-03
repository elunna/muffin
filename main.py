#!/usr/bin/env python
"""
Main entry point.
"""
import argparse


def main():
    print('Hello world!')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', help='increase output verbosity', action="store_true")
    args = parser.parse_args()

    if args.verbose:
        main()
