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
Tests for write_license(config)
"""


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
    write_license(GNU_CONFIG)
    assert os.path.exists(lic_path)  # LICENSE file doesn't exist

"""
Tests for cp_templates(project_name)
"""


def test_cptemplate_makes_project_dir():
    cp_templates(MIT_CONFIG)
    assert os.path.isdir(TEST_PROJ)  # Error making project dir


def test_cptemplate__subdirs():
    # Uses a test generator to go through all the subdirectories we want to test.
    for i in SUBDIRS:
        subdir = TEST_PROJ + '/' + i
        yield check_dir, subdir


def check_dir(d):
    # This has to go here bc cleanup get called before and after this method.
    cp_templates(MIT_CONFIG)
    assert os.path.isdir(d)  # Directory doesn't exist


def test_cptemplates_gitignore_exists():
    cp_templates(MIT_CONFIG)
    assert os.path.exists(TEST_PROJ + '/.gitignore')    # .gitignore not created


def test_cptemplates_env_exists():
    cp_templates(MIT_CONFIG)
    assert os.path.exists(TEST_PROJ + '/.env')       # Error making main.py


def test_cptemplates_konchrc_exists():
    cp_templates(MIT_CONFIG)
    assert os.path.exists(TEST_PROJ + '/.konchrc')       # Error making main.py


def test_cptemplates_pytest_ini_exists():
    cp_templates(MIT_CONFIG)
    assert os.path.exists(TEST_PROJ + '/pytest.ini')       # Error making main.py


def test_cptemplates_main_py_exists():
    cp_templates(MIT_CONFIG)
    assert os.path.exists(TEST_PROJ + '/main.py')       # Error making main.py


def test_cptemplates_logger_py_exists():
    cp_templates(MIT_CONFIG)
    assert os.path.exists(TEST_PROJ + '/src/logger.py')  # Error making /src/logger.py


def test_cptemplates_init_files():
    init_files = ['/', '/src', '/tests']

    # Uses a test generator to go through all the init files we want to test.
    for i in init_files:
        init = TEST_PROJ + i + '/__init__.py'
        yield check_init_file, init


def check_init_file(filename):
    cp_templates(MIT_CONFIG)
    assert os.path.exists(filename)  # Filename doesn't exist
