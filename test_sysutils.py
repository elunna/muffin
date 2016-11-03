import os
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
# chk_sys_for('weirdo')

"""
Tests for chk_pip_for(lib)
"""

"""
Tests for chk_python()
"""

"""
Tests for new_virtualenv(py_version)
"""

"""
Tests for touch_test()
"""
