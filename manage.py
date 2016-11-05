"""
Inspired by the Django manage - a tool to manage mundane project tasks.
"""


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
