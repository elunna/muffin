import os
import shutil
import pystart
import pytest
"""
Tests for setup_dirs()
"""
TEST_PROJ = 'testproject/'


def rm_dir():
    if os.path.isdir(TEST_PROJ):
        shutil.rmtree(TEST_PROJ)


@pytest.yield_fixture(autouse=True)
def cleanup():
    rm_dir()
    yield None
    rm_dir()

"""
Tests for setup_dirs(projectname)
"""


def test_setupdirs_makes_project_dir():
    pystart.setup_dirs(TEST_PROJ)
    assert os.path.isdir(TEST_PROJ)  # Error making project dir


def test_setupdirs_subdirs():
    # Uses a test generator to go through all the subdirectories we want to test.
    for i in pystart.SUBDIRS:
        subdir = TEST_PROJ + i
        yield check_dir, subdir


def check_dir(d):
    # This has to go here bc cleanup get called before and after this method.
    pystart.setup_dirs(TEST_PROJ)
    assert os.path.isdir(d)  # Directory doesn't exist


"""
Tests for make_readme(info_dict)
"""


def test_makereadme_empty():
    pystart.setup_dirs(TEST_PROJ)
    f = TEST_PROJ + 'README.md'
    proj = {'homedir': TEST_PROJ}
    pystart.make_readme(proj)  # README.md was not created in project/
    assert os.path.exists(f)
