""" Tests for the muffin module. """
import os
import pytest
from .muffin import *
from test_configs import *


@pytest.yield_fixture(autouse=True)
def cleanup():
    wipe_dir(TEST_PROJ)
    yield None
    wipe_dir(TEST_PROJ)


def test_wipedir_created_dir_dne():
    testdir = 'some_random_directory_xxx1234'
    ensure_dir(testdir)
    wipe_dir(testdir)
    assert os.path.isdir(testdir) is False


def test_ensuredir_exists():
    testdir = 'some_random_directory_xxx1234'
    ensure_dir(testdir)
    assert os.path.isdir(testdir)
    wipe_dir(testdir)


def test_writelicense_MIT():
    ensure_dir(TEST_PROJ)
    lic_path = TEST_PROJ + '/LICENSE'
    write_license(MIT_CONFIG)
    assert os.path.exists(lic_path)  # LICENSE file doesn't exist


def test_writelicense_GNU():
    ensure_dir(TEST_PROJ)
    lic_path = TEST_PROJ + '/LICENSE'
    write_license(GNU_CONFIG)
    assert os.path.exists(lic_path)  # LICENSE file doesn't exist


def test_writelicense_WTFPL():
    ensure_dir(TEST_PROJ)
    lic_path = TEST_PROJ + '/LICENSE'
    write_license(WTFPL_CONFIG)
    assert os.path.exists(lic_path)  # LICENSE file doesn't exist


def test_makesetupsh_exists():
    make_setup_sh(FULL_CONFIG)
    assert os.path.exists(FULL_CONFIG['projectname'] + '/setup.sh')  # Error making setup.sh


def test_setupgit_git_dir_exists():
    setup_git(FULL_CONFIG)
    assert os.path.isdir(FULL_CONFIG['projectname'] + '/.git')                 # Error making .git dir


def test_setupgit_git_config_exists():
    setup_git(FULL_CONFIG)
    assert os.path.exists(FULL_CONFIG['projectname'] + '/.git/config')         # Error making .git/config


def test_cptemplate_makes_project_dir():
    cp_templates(FULL_CONFIG)
    assert os.path.isdir(TEST_PROJ)  # Error making project dir


def test_cptemplate__subdirs():
    # Uses a test generator to go through all the subdirectories we want to test.
    for i in SUBDIRS:
        subdir = TEST_PROJ + '/' + i
        yield check_dir, subdir


def check_dir(d):
    # This has to go here bc cleanup get called before and after this method.
    cp_templates(FULL_CONFIG)
    assert os.path.isdir(d)  # Directory doesn't exist


def test_cptemplates_gitignore_exists():
    cp_templates(FULL_CONFIG)
    assert os.path.exists(TEST_PROJ + '/.gitignore')    # .gitignore not created


def test_cptemplates_env_exists():
    cp_templates(FULL_CONFIG)
    assert os.path.exists(TEST_PROJ + '/.env')       # Error making main.py


def test_cptemplates_konchrc_exists():
    cp_templates(FULL_CONFIG)
    assert os.path.exists(TEST_PROJ + '/.konchrc')       # Error making main.py


def test_cptemplates_pytest_ini_exists():
    cp_templates(FULL_CONFIG)
    assert os.path.exists(TEST_PROJ + '/pytest.ini')       # Error making main.py


def test_cptemplates_main_py_exists():
    cp_templates(FULL_CONFIG)
    assert os.path.exists(TEST_PROJ + '/main.py')       # Error making main.py


def test_cptemplates_logger_py_exists():
    cp_templates(FULL_CONFIG)
    assert os.path.exists(TEST_PROJ + '/src/logger.py')  # Error making /src/logger.py


def test_cptemplates_init_files():
    init_files = ['/', '/src', '/tests']

    # Uses a test generator to go through all the init files we want to test.
    for i in init_files:
        init = TEST_PROJ + i + '/__init__.py'
        yield check_init_file, init


def check_init_file(filename):
    cp_templates(FULL_CONFIG)
    assert os.path.exists(filename)  # Filename doesn't exist


def test_saveconfig_exists():
    save_config(FULL_CONFIG)
    projectdir = FULL_CONFIG['projectname']
    assert os.path.isdir(projectdir)  # Project directory doesn't exist
    assert os.path.exists(projectdir + '/config.json')  # config.json doesn't exist
