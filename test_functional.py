import os
import muffin
import test_configs

"""
Functional tests for muffinX.

muffinX is a Python project templating engine. It is for quickly and efficiently setting up
projects that are ready for professional use.
"""


def test_newproject():
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
    muffin.new_project(test_configs.MIT_CONFIG)
    ROOT = test_configs.MIT_CONFIG['projectname'] + '/'

    # The directory structure (unit tested)
    assert os.path.isdir(ROOT + '')                     # Error making root dir
    assert os.path.isdir(ROOT + 'src')                  # Error making src dir
    assert os.path.isdir(ROOT + 'tests')                # Error making tests dir
    assert os.path.isdir(ROOT + 'data')                 # Error making data dir
    assert os.path.isdir(ROOT + 'temp')                 # Error making temp dir

    # __init__ files in the root, src, and tests directories.
    assert os.path.exists(ROOT + '__init__.py')         # Error making root __init__.py
    assert os.path.exists(ROOT + 'src/__init__.py')     # Error making src __init__.py
    assert os.path.exists(ROOT + 'tests/__init__.py')   # Error making tests __init__.py

    # Check for customized files
    assert os.path.exists(ROOT + 'README.md')           # Error making README.md
    assert os.path.exists(ROOT + 'LICENSE')             # Error making LICENSE

    # Check for files from templates
    assert os.path.exists(ROOT + '.gitignore')          # Error copying .gitignore
    assert os.path.exists(ROOT + '.env')                # Error copying .env
    assert os.path.exists(ROOT + '.konchrc')            # Error copying .konchrc
    assert os.path.exists(ROOT + 'pytest.ini')          # Error copying pytest.ini

    # Check for templated .py files
    assert os.path.exists(ROOT + 'main.py')             # Error copying main.py
    assert os.path.exists(ROOT + 'src/logger.py')       # Error copying utils.py

    # Check git
    assert os.path.isdir(ROOT + '.git')                 # Error making .git dir
    assert os.path.exists(ROOT + '.git/config')         # Error making .git/config
    # Check hooks were copied

    muffin.wipe_dir(ROOT)  # Cleanup


def test_setup_project_env():
    # Setup Python 2.7 env
    muffin.setup_project_env(test_configs.VENV_CONFIG)
    ROOT = test_configs.MIT_CONFIG['projectname'] + '/'

    # Check that the setup.sh file was created.
    assert os.path.exists(ROOT + 'setup.sh')            # Error making setup.sh

    # Check that pip was upgraded?

    # Check essential system and pip libraries
    #  assert sysutils.chk_sys_libraries()
    #  assert sysutils.chk_pip_libraries()              # Should be run in the virtualenv

    muffin.wipe_dir(ROOT)  # Cleanup
