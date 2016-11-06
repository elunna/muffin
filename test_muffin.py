import os
import pytest
from muffin import *
from test_configs import *

"""
Tests for setup_dirs()
"""


@pytest.yield_fixture(autouse=True)
def cleanup():
    wipe_dir(TEST_PROJ)
    yield None
    wipe_dir(TEST_PROJ)

"""
Tests for setup_dirs(projectname)
"""


def test_setupdirs_makes_project_dir():
    setup_dirs(TEST_PROJ)
    assert os.path.isdir(TEST_PROJ)  # Error making project dir


def test_setupdirs_subdirs():
    # Uses a test generator to go through all the subdirectories we want to test.
    for i in SUBDIRS:
        subdir = TEST_PROJ + '/' + i
        yield check_dir, subdir


def check_dir(d):
    # This has to go here bc cleanup get called before and after this method.
    setup_dirs(TEST_PROJ)
    assert os.path.isdir(d)  # Directory doesn't exist

"""
Tests for setup_init_files(projectname)
"""


def test_setupinitfiles():
    init_files = ['/', '/src', '/tests']

    # Uses a test generator to go through all the init files we want to test.
    for i in init_files:
        init = TEST_PROJ + i + '/__init__.py'
        yield check_init_file, init


def check_init_file(filename):
    setup_dirs(TEST_PROJ)
    setup_init_files(TEST_PROJ)
    assert os.path.exists(filename)  # Filename doesn't exist

"""
Tests for write_license(config)
"""


def test_writelicense_MIT():
    setup_dirs(TEST_PROJ)
    lic_path = TEST_PROJ + '/LICENSE'
    write_license(MIT_CONFIG)
    assert os.path.exists(lic_path)  # LICENSE file doesn't exist


def test_writelicense_GNU():
    setup_dirs(TEST_PROJ)
    lic_path = TEST_PROJ + '/LICENSE'
    write_license(GNU_CONFIG)
    assert os.path.exists(lic_path)  # LICENSE file doesn't exist

"""
Tests for cp_templates(project_name)
"""

# cp_templates when dir does not exist?


def test_cptemplates_gitignore_exists():
    setup_dirs(TEST_PROJ)
    cp_templates(TEST_PROJ)
    assert os.path.exists(TEST_PROJ + '/.gitignore')    # .gitignore not created


def test_cptemplates_env_exists():
    setup_dirs(TEST_PROJ)
    cp_templates(TEST_PROJ)
    assert os.path.exists(TEST_PROJ + '/.env')       # Error making main.py


def test_cptemplates_konchrc_exists():
    setup_dirs(TEST_PROJ)
    cp_templates(TEST_PROJ)
    assert os.path.exists(TEST_PROJ + '/.konchrc')       # Error making main.py


def test_cptemplates_pytest_ini_exists():
    setup_dirs(TEST_PROJ)
    cp_templates(TEST_PROJ)
    assert os.path.exists(TEST_PROJ + '/pytest.ini')       # Error making main.py


def test_cptemplates_main_py_exists():
    setup_dirs(TEST_PROJ)
    cp_templates(TEST_PROJ)
    assert os.path.exists(TEST_PROJ + '/main.py')       # Error making main.py


def test_cptemplates_logger_py_exists():
    setup_dirs(TEST_PROJ)
    cp_templates(TEST_PROJ)
    assert os.path.exists(TEST_PROJ + '/src/logger.py')  # Error making utils.py
