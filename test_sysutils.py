import os
import pystart
import pytest
import sysutils


"""
Tests for cmd_result(cmd)
"""


def test_cmdresult_touch():
    testfile = 'tempfile.xxx'
    if os.path.exists(testfile):
        os.remove(testfile)
    cmd = ['touch', testfile]
    result = sysutils.cmd_result(cmd)
    assert result is True
    assert os.path.exists(testfile)

    os.remove(testfile)  # Cleanup the file

"""
Tests for chk_sys_for(app)
"""


def test_chksysfor_nonexistant():
    cmd = 'weirdo'
    expected = False
    assert sysutils.chk_sys_for(cmd) == expected


def test_chksysfor_ls():
    # Every linux system has ls
    cmd = 'ls'
    expected = True
    assert sysutils.chk_sys_for(cmd) == expected


"""
Tests for chk_pip_for(lib)
"""


def test_chkpipfor_nonexistant():
    cmd = 'weirdo'
    expected = False
    assert sysutils.chk_pip_for(cmd) == expected


def test_chkpipfor_pip():
    # If we have pip, it should almost certainly show it!
    cmd = 'pip'
    expected = True
    assert sysutils.chk_pip_for(cmd) == expected


"""
Tests for chk_python()
"""
py2version = pytest.mark.skipif(sysutils.chk_sys_for('python2') is False,
                                reason="python2 required")

py3version = pytest.mark.skipif(sysutils.chk_sys_for('python3') is False,
                                reason="python3 required")


@py2version
def test_chkpython_2():
    result = sysutils.chk_python()
    assert '2.7' in result


@py3version
def test_chkpython_3():
    result = sysutils.chk_python()
    assert '2.7' in result


"""
Tests for new_virtualenv(py_version)
"""


def test_newvirtualenv_py1():
    VENV = 'venv_test1_0'
    py = '1.0'  # This is not available, even in the older releases.
    sysutils.new_virtualenv(py, name=VENV)
    assert os.path.isdir(VENV) is False        # Should not create any dir.


@py2version
@pytest.mark.skip(reason="works - but uses lots of memory/files")
def test_newvirtualenv_py2_7():
    VENV = 'venv_test2_7'
    py = '2.7'
    result = sysutils.new_virtualenv(py, name=VENV)
    assert result is True  # 11_3_16: This is currently a false positive, but leaving it anyway.

    # Check that the virtual env directory was created
    assert os.path.isdir(VENV)        # Error making virtual env directory.

    # Check that the python2.7 bin is present
    pythonbin = VENV + '/bin/python2.7'
    assert os.path.exists(pythonbin)  # Error making .env

    pystart.wipe_dir(VENV)   # Clean it up


"""
Tests for touch_test()
"""
