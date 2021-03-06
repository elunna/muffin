#!/usr/bin/env python
"""
  " Inspired by the Django manage - a tool to manage mundane project tasks.
  """
import argparse
import json
import subprocess


def clean():
    """ Cleans out non-essential project files:
        From directories: /data, /temp, /logs directories
        Removes .ropeproject, __pycache__, .cache directories
        Removes all *.pyc files.
    """
    commands = [
        'rm -v data/*',
        'rm -v temp/*',
        'rm -v logs/*',
        'rm -rf .cache',
        'find . -type f -name "*.py[co]" -delete',
        'find . -type d -name "__pycache__" -delete 2>/dev/null',
        #  'find . -type d -name ".cache" -delete',
        #  'find . -type d -name ".ropeproject" -delete',
    ]
    for cmd in commands:
        x = subprocess.call(cmd, shell=True)
        print('{}: exit {}'.format(cmd, x))


def archive():
    """ Zip up the /data directory, and optionally the logs directory """


def newmod():
    """ Create basic templates for a new module and test """


def freeze():
    """ Create or replace the requirements.txt from pip.  """
    cmd = 'pip freeze > requirements.txt'
    subprocess.call(cmd, shell=True)


def setup_sphinx(conf):
    """ Sets up the Sphinx documentation with as many defaults as possible. """
    cmd = [
        'sphinx-quickstart',
        '--sep',
        '--dot=_',
        '-p', conf.get('projectname', ''),
        '-a', conf.get('author', ''),
        '-v', '1.0',
        '-r', '1.0',
        '-l', 'en',
        '--suffix=.rst',
        '--master=index',
        '--ext-autodoc',
        '--ext-doctest',
        '--ext-viewcode',
        '--makefile',
        '--no-batchfile',
        'doc',
    ]
    subprocess.call(cmd)
    print('Sphinx docs should have setup a /doc directory.')
    print("Run '$ /doc/make html' to build the docs.")


def get_defaults():
    """ Retrieves the settings the user entered during the project setup wizard."""
    with open('config.json', 'r') as f:
        contents = f.read()
        defaults = json.loads(contents)
    return defaults


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Helper utility for managing mundane project tasks.")

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-c', '--clean', action='store_true',
                       help="Clean up __pycache__, .ropeprojects, .cache dirs, and .pyc files.")

    group.add_argument('-m', '--makedocs', action='store_true',
                       help="Gets the Sphinx docs setup up and ready for building.")

    group.add_argument('-s', '--servedocs', action='store_true',
                       help="Serves up the Sphinx docs in the localserver.")

    args = parser.parse_args()

    if args.clean:
        clean()
    elif args.makedocs:
        setup_sphinx(get_defaults())
