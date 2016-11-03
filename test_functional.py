import os
import pystart
import test_pystart
import pytest

"""
Functional tests for pystart.

Pystart is a Python project templating engine. It is for quickly and efficiently setting up
projects that are ready for professional use.
"""


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
    pystart.new_project(test_pystart.MIT_CONFIG)
    project_name = test_pystart.MIT_CONFIG['projectname']

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

    # Check that the LICENSE was copied
    assert os.path.exists(project_name + '/LICENSE')  # Error making LICENSE

    # Cleanup
    test_pystart.wipe_project()


def test_sys_requirements():
    # After a new project, we should have all these basic things:
    # python2(or 3 depending)
    # virtualenv
    # autoenv
    # pip,
    # py.test
    # konch
    pytest.fail()


def test_virtualenv_py2():
    # Make a python 2.7 env
    # Setup the basic project
    pystart.new_project(test_pystart.VENV_CONFIG)
    ROOT = test_pystart.MIT_CONFIG['projectname'] + '/'

    # Check that we can enter the virtualenv and activate it

    # Check that the venv is python 2.7

    # Check that pip was upgraded?

    # Check that the .env file was created
    assert os.path.exists(ROOT + '.env')  # Error making .env
