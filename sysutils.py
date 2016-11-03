import subprocess
import os


def is_tool(cmd):
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
    result = is_tool(cmd)
    print('{:30} installed: {}'.format(cmd[0], result))
    return result


def chk_pip_for(lib):
    """
    Returns True if the library is installed in pip, False otherwise.
    This is installed by pip.
    """
    cmd = ['pip', 'show', lib]
    try:
        ls_output = subprocess.check_output(cmd)
        result = len(ls_output) > 0
        #  print(ls_output)
        print('{:30} installed: {}'.format(cmd[2], result))
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

if __name__ == "__main__":
    print('\n##### System libraries')
    chk_sys_for('python')
    chk_sys_for('python3')
    chk_sys_for('pip')
    chk_sys_for('git')
    chk_sys_for('virtualenv')
    chk_sys_for('weirdo')

    print('\n##### pip libraries')
    chk_pip_for('konch')
    chk_pip_for('autoenv')
    chk_pip_for('weirdo')

    # Versions of python installed
    print('\nPython Versions')

    versions = chk_python()
    for v in sorted(versions):
        py = 'python{}'.format(v)
        print('{:30} installed: True'.format(py))
