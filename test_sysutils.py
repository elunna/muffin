import os
import muffin
import pytest
import sysutils


"""
Tests for run_cmd_result(cmd)
"""


def test_cmdexists_touch_returnsTrue():
    testfile = 'tempfile.xxx'
    result = sysutils.cmd_exists(['touch', testfile])
    assert result is True
    assert os.path.exists(testfile)

    os.remove(testfile)  # Cleanup the file


def test_cmdexists_ls_returnsTrue():
    result = sysutils.cmd_exists(['ls'])
    assert result is True


def test_cmdexists_ls_everything_returnsTrue():
    # It may not be a valid argument, but the cmd exists
    result = sysutils.cmd_exists(['ls', '--everything'])
    assert result is True


def test_cmdexists_twilicane_returnsFalse():
    result = sysutils.cmd_exists(['twilicane'])
    assert result is False


"""
Tests for run_cmd_success(cmd)
"""


def test_runcmdsuccess_touch():
    testfile = 'tempfile.xxx'
    result = sysutils.run_cmd_success(['touch', testfile])
    assert result is True
    os.remove(testfile)  # Cleanup the file


def test_runcmdsuccess_touch_invalid_arg():
    result = sysutils.run_cmd_success(['touch', '-XXX'])
    assert result is False


def test_runcmdsuccess_invalid_cmd_returneFalse():
    result = sysutils.run_cmd_success(['twilicane'])
    assert result is False


"""
Tests for run_cmd_in_dir(cmd)
"""


def test_runcmdindir_invaliddir_returnsTrue():
    _dir = 'nonexistant/'
    testfile = 'tempfile.xxx'
    result = sysutils.run_cmd_in_dir(['touch', testfile], _dir)
    assert result is False


def test_runcmdindir_valid_returnsFalse():
    _dir = 'rundir/'
    testfile = 'tempfile.xxx'
    muffin.ensure_dir(_dir)
    result = sysutils.run_cmd_in_dir(['touch', testfile], _dir)

    assert result is True
    assert os.path.exists(_dir + testfile)

    muffin.wipe_dir(_dir)


def test_runcmdindir_badcmd_returnsFalse():
    _dir = 'rundir/'
    muffin.ensure_dir(_dir)
    result = sysutils.run_cmd_in_dir(['twilicane'], _dir)
    assert result is False
    muffin.wipe_dir(_dir)

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
    name = 'venv_test1_0'
    py = '1.0'  # This is not available, even in the older releases.
    sysutils.new_virtualenv(py, projectname=name)
    assert os.path.isdir(name + '/venv') is False        # Should not create any dir.


@py2version
#  @pytest.mark.skip(reason="works - but uses lots of memory/files")
def test_newvirtualenv_py2_7():
    name = 'venv_test2_7'
    py = '2.7'
    sysutils.new_virtualenv(py, projectname=name)

    # Check that the virtual env directory was created
    assert os.path.isdir(name + '/venv')        # Error making virtual env directory.

    # Check that the python2.7 bin is present
    pythonbin = name + '/venv/bin/python2.7'
    assert os.path.exists(pythonbin)  # Error making .env

    muffin.wipe_dir(name)   # Clean it up

# Note: Python 3.4 and 3.5 environment tests in test_functional.py
