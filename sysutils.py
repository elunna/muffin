import subprocess
import os
import pystart

VENV_DIR = 'venv'
SYS_LIBS = ['python', 'python3', 'pip', 'git', 'virtualenv']


def cmd_result(cmd):
    # Python 3.3+: can use subprocess.DEVNULL rather than open(os.devnull).
    try:
        devnull = open(os.devnull, 'w')
        subprocess.Popen(cmd, stdout=devnull, stderr=devnull).communicate()
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            return False
    return True


def cmd_success(cmd):
    result = subprocess.call(cmd)
    pass
    if result:
        return False
    else:
        return True


def chk_sys_for(app):
    """
    Returns True if the library is installed in the linux system, False otherwise.
    This is installed by pip.
    """
    cmd = [app, '--version']
    result = cmd_result(cmd)
    return result


def run_setup_script(_dir):
    cmd = ['sh', 'setup.sh']
    subprocess.Popen(cmd, cwd=_dir)


def chk_pip_for(lib):
    """
    Returns True if the library is installed in pip, False otherwise.
    This is installed by pip.
    """
    cmd = ['pip', 'show', lib]
    try:
        ls_output = subprocess.check_output(cmd)
        if len(ls_output) > 0:
            return True
        else:
            return False
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            return False


def chk_sys_libraries():
    """Essential libraries to get this template engine working."""
    # Add pip3?
    for l in SYS_LIBS:
        if chk_sys_for(l) is False:
            print('{} is not installed, this is required.'.format(l))
            return False
        else:
            print('{:30} is installed'.format(l))
    else:
        return True


def chk_pip_libraries(py_ver):
    """Core pip libraries that should be in the virtualenv after setup."""
    pip_libs = pystart.PY_MODULES[py_ver]
    for l in pip_libs:
        if chk_pip_for(l) is False:
            print('{} is not installed, this is required for Python{}.'.format(l, py_ver))
            return False
        else:
            print('{:30} is installed'.format(l))
    else:
        return True


def chk_python():
    """Returns which versions of Python are installed, as a list (ie: ['2.7', '3.5'])"""
    cmd = ['whereis', 'python']
    output = subprocess.check_output(cmd).split()

    PYTHON_DIR = '/usr/local/lib/'
    # Filter out anything that doesn't start with /
    output = [x for x in output if x.startswith(PYTHON_DIR)]

    trimthis = '/usr/local/lib/python'

    return [x.replace(trimthis, '') for x in output]


def new_virtualenv(py_version, projectname):
    VENV = projectname + '/venv'
    # virtualenv checks the python ver so we don't have to worry about that :)
    cmd = ['virtualenv', '--python=python{}'.format(py_version), VENV]
    return cmd_result(cmd)


if __name__ == "__main__":
    chk_sys_libraries()
    chk_pip_libraries('2.7')
