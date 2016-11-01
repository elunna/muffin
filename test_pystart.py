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


def test_setupdirs_makes_project_dir():
    pystart.setup_dirs(TEST_PROJ)
    assert os.path.isdir(TEST_PROJ)  # Error making project dir
    cleanup()


def test_setupdirs_src_dir():
    pystart.setup_dirs(TEST_PROJ)
    srcdir = TEST_PROJ + 'src'  # Error making project/src dir
    assert os.path.isdir(srcdir)
    cleanup()


def test_setupdirs_data_dir():
    pystart.setup_dirs(TEST_PROJ)
    srcdir = TEST_PROJ + 'data'
    assert os.path.isdir(srcdir)  # Error making project/data dir
    cleanup()


def test_setupdirs_tests_dir():
    pystart.setup_dirs(TEST_PROJ)
    srcdir = TEST_PROJ + 'tests'
    assert os.path.isdir(srcdir)  # Error making project/tests dir
    cleanup()


def test_setupdirs_temp_dir():
    pystart.setup_dirs(TEST_PROJ)
    srcdir = TEST_PROJ + 'temp'
    assert os.path.isdir(srcdir)  # Error making project/temp dir
    cleanup()
