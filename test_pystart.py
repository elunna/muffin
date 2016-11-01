import os
import shutil
import pystart
import pytest
"""
Tests for setup_dirs()
"""
TEST_PROJ = 'testproject/'


@pytest.yield_fixture(autouse=True)
def cleanup():
    yield None
    if os.path.isdir(TEST_PROJ):
        shutil.rmtree(TEST_PROJ)


def test_setupdirs_makes_project_dir():
    pystart.setup_dirs(TEST_PROJ)
    assert os.path.isdir(TEST_PROJ)
    cleanup()


def test_setupdirs_src_dir():
    pystart.setup_dirs(TEST_PROJ)
    srcdir = TEST_PROJ + 'src'
    assert os.path.isdir(srcdir)
    cleanup()
