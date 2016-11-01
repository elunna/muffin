import os
import pystart
"""
Tests for setup_dirs()
"""


def test_setupdirs_makes_project_dir():
    p = 'testproject'
    pystart.setup_dirs(p)
    assert os.path.isdir(p)
