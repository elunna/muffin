import subprocess
import os

VENV_DIR = 'venv'


def cmd_result(cmd):
    # Python 3.3+: can use subprocess.DEVNULL rather than open(os.devnull).
    try:
        devnull = open(os.devnull, 'w')
        subprocess.Popen(cmd, stdout=devnull, stderr=devnull).communicate()
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            return False
    return True


def chk_sys_for(app):
    """
    Returns True if the library is installed in the linux system, False otherwise.
    This is installed by pip.
    """
    cmd = [app, '--version']
    result = cmd_result(cmd)
    #  print('{:30} installed: {}'.format(cmd[0], result))
    return result


def chk_pip_for(lib):
    """
    Returns True if the library is installed in pip, False otherwise.
    This is installed by pip.
    """
    cmd = ['pip', 'show', lib]
    try:
        ls_output = subprocess.check_output(cmd)
        #  result = len(ls_output) > 0
        #  print(ls_output)
        #  print('{:30} installed: {}'.format(cmd[2], result))
        if len(ls_output) > 0:
            return True
        else:
            return False
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            return False


def chk_python():
    cmd = ['whereis', 'python']
    output = subprocess.check_output(cmd).split()

    PYTHON_DIR = '/usr/local/lib/'
    # Filter out anything that doesn't start with /
    output = [x for x in output if x.startswith(PYTHON_DIR)]

    trimthis = '/usr/local/lib/python'

    # Return just the version numbers in a list (ie: ['2.7', '3.5']
    return [x.replace(trimthis, '') for x in output]


def new_virtualenv(py_version, projectname):
    VENV = projectname + '/venv'
    # virtualenv checks the python ver so we don't have to worry about that :)
    cmd = ['virtualenv', '--python=python{}'.format(py_version), VENV]
    return cmd_result(cmd)


def chk_sys_libraries():
    """Essential libraries to get this template engine working."""
    # Add pip3?
    libs = ['python', 'python2', 'python3', 'pip', 'git', 'virtualenv']
    for l in libs:
        if chk_sys_for(l) is False:
            print('{} is not installed, this is required.'.format(l))
            return False
    else:
        return True


def chk_pip_libraries():
    """Core pip libraries that should be in the virtualenv after setup."""
    libs = ['pip', 'pytest', 'konch', 'autoenv']
    for l in libs:
        if chk_pip_for(l) is False:
            print('{} is not installed, this is required.'.format(l))
            return False
    else:
        return True
