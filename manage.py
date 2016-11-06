"""
Inspired by the Django manage - a tool to manage mundane project tasks.
"""
import json
import subprocess


def clean():
    """
    Cleans out non-essential project files:
        * /data
        * /temp
        * /logs directories
        *.pyc files.
    """


def archive():
    """
    Zip up the /data directory, and optionally the logs directory
    """


def newmod():
    """
    Create basic templates for a new module and test
    """


def freeze():
    """
    Create or replace the requirements.txt from pip.
    """
    cmd = 'pip freeze > requirements.txt'
    subprocess.call(cmd, shell=True)


def setup_sphinx(config):
    cmd = [
        'sphinx-quickstart',
        '--sep',
        '--dot=_',
        '-p', config.get('projectname', ''),
        '-a', config.get('author', ''),
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
    with open('config.json', 'r') as f:
        contents = f.read()
        defaults = json.loads(contents)
    return defaults


if __name__ == "__main__":
    setup_sphinx(get_defaults())
