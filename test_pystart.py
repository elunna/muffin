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
    assert os.path.isdir(TEST_PROJ)
    cleanup()


def test_setupdirs_src_dir():
    pystart.setup_dirs(TEST_PROJ)
    srcdir = TEST_PROJ + 'src'
    assert os.path.isdir(srcdir)
    cleanup()
