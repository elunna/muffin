import os
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


@py2version
def test_chkpython_2():
    result = sysutils.chk_python()
    assert '2.7' in result

py3version = pytest.mark.skipif(sysutils.chk_sys_for('python3') is False,
                                reason="python3 required")


@py3version
def test_chkpython_3():
    result = sysutils.chk_python()
    assert '2.7' in result


"""
Tests for new_virtualenv(py_version)
"""


def test_newvirtualenv_py2_7():
    venv = 'TEST_ENV'
    # Check that the virtual env directory was created
    assert os.path.isdir(venv)        # Error making virtual env directory.

    # Check that the python2.7 bin is present
    pythonbin = venv + '/bin/python2.7'
    assert os.path.exists(pythonbin)  # Error making .env


    wipe_venv(venv)   # Clean it up


"""
Tests for touch_test()
"""
