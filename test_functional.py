import os
import pystart
import test_pystart

"""
Functional tests for pystart.

Pystart is a Python project templating engine. It is for quickly and efficiently setting up
projects that are ready for professional use.
"""

STARTDICT = {
    'projectname': test_pystart.TEST_PROJ,
    'author': 'erik',
    'purpose': 'testing pystart',
    'license': 'MIT',
}


def test_wizard():
    """
    Erik wants to start a new project, nothing fancy, but it should at least have this:
        * A modern Directory
            root_project_dir/
                /src
                /tests
                /data
                /temp
        * README.md for git
        * .gitigore for git
    The README.md and .gitignore are essential, but annoying to make, so he would rather stream-
    line the creation and make life as painless as possible - I mean, there is code to be written!

    Erik starts : $ python startpy.py

    He is presented with a wizard which asks him all the basic info.
    After completing the wizard we should have a few things:
    """
    pystart.new_project(STARTDICT)
    project_name = STARTDICT['projectname']

    # The directory structure (unit tested)
    assert os.path.isdir(project_name + '/')        # Error making root dir
    assert os.path.isdir(project_name + '/src')     # Error making src dir
    assert os.path.isdir(project_name + '/tests')   # Error making tests dir
    assert os.path.isdir(project_name + '/data')    # Error making data dir
    assert os.path.isdir(project_name + '/temp')    # Error making temp dir

    # __init__ files in the root, src, and tests directories.
    assert os.path.exists(project_name + '/__init__.py')         # Error making root __init__.py
    assert os.path.exists(project_name + '/src/__init__.py')     # Error making src __init__.py
    assert os.path.exists(project_name + '/tests/__init__.py')   # Error making tests __init__.py

    # README.md.
    assert os.path.exists(project_name + '/README.md')   # Error making README.md

    # .gitignore
    assert os.path.exists(project_name + '/.gitignore')  # Error making .gitignore

    # Cleanup
    # test_python.TEST_PROJ,
    test_pystart.wipe_project()


def usecase_wizard():
    # The wizard use a defaults.py for author and license type.
    pass
