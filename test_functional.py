import pystart
"""
Functional tests for pystart.

Pystart is a Python project templating engine. It is for quickly and efficiently setting up
projects that are ready for professional use.
"""


def test_wizard():
    """
    Erik wants to start a new project.
    He just wants the core directory structure and README setup so he can start a git repo quickly.
    Erik starts : $ python startpy.py
    He is presented with a wizard which asks him all the basic info:

    After completing the wizard we should have a dict
    """
    startdict = pystart.wizard()

    # Dict should have the project name
    assert 'name' in startdict

    # Dict should have the author
    assert 'author' in startdict

    # Dict should have the project purpose
    assert 'purpose' in startdict

    # Dict should have the start date
    assert 'start' in startdict

    # Dict should have the end date
    #   (anything is permissiable - perhaps small parser to do dates or length of time later)
    assert 'end' in startdict

    # Dict should have the license type(ex:[MIT, GNU])
    assert 'license' in startdict

    # The project then generates the directory structure (unit tested)

    # The wizard dict is then used to generate the README.md.
    # The README should have all the info from the wizard but in markdown format.


def usecase_wizard():
    # The wizard use a defaults.py for author and license type.
    pass
