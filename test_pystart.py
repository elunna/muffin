import os
import shutil
import pystart
"""
Tests for setup_dirs()
"""
TEST_PROJ = 'testproject/'


def cleanup():
    if os.path.isdir(TEST_PROJ):
        shutil.rmtree(TEST_PROJ)


def test_setupdirs_makes_project_dir():
    pystart.setup_dirs(TEST_PROJ)
    assert os.path.isdir(TEST_PROJ)
    cleanup()
