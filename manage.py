"""
Inspired by the Django manage - a tool to manage mundane project tasks.
"""
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
    result = sysutils.cmd_success(cmd)
    if result:
        print('Sphinx docs should have setup a /doc directory.')
        print("Run 'make html' to build the docs.")
    else:
        print('Error setting up Sphinx docs :(')


if __name__ == "__main__":
    pass
