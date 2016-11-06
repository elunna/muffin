import argparse
import json
import licenses
import os
import readme
import shutil
import sysutils
import wizard

SUBDIRS = ['src', 'tests', 'data', 'temp', 'logs']
TEMPLATE_DIR = 'templates/'
CORE_MODULES = ['konch', 'ipython', 'pytest', 'sphinx']

PY_MODULES = {
    # We need the security libraries because older versions of py2 don't have good ssl.
    '2.7': ['urllib3[secure]', 'requests[security]'] + CORE_MODULES,
    '3.4': [] + CORE_MODULES,
    '3.5': [] + CORE_MODULES,
}

XTRA_MODULES = ['beautifulsoup4', 'scrapy', 'requests', 'django', 'selenium']


def setup_dirs(projectname):
    # Create main project directory
    os.makedirs(projectname)

    for sub in SUBDIRS:
        # Create each subdirectory
        os.makedirs(projectname + '/' + sub)


def wipe_dir(venv):
    if os.path.isdir(venv):
        shutil.rmtree(venv)


def ensure_dir(_dir):
    if not os.path.exists(_dir):
        os.makedirs(_dir)


def setup_init_files(projectname):
    # Make __init__.py files
    init_files = [
        '/__init__.py',
        '/src/__init__.py',
        '/tests/__init__.py'
    ]
    for i in init_files:
        filename = projectname + i
        open(filename, 'w').close()


def write_license(config):
    text = licenses.get(config['license'])
    filename = config['projectname'] + '/LICENSE'
    with open(filename, 'w') as f:
        f.write(text)


def make_setup_files(config):
    # Make setup.sh
    setupfile = config['projectname'] + '/setup.sh'
    pip_installs = PY_MODULES[config['python']] + config.get('modules', [])

    with open(setupfile, 'w') as f:
        f.write("#!/bin/bash\n")
        f.write("# Purpose: Installs the required modules for {}.\n".format(config['projectname']))
        f.write('/bin/bash -c ". venv/bin/activate; ')

        # Check the core system utilities needed
        for i in sysutils.SYS_LIBS:
            if not sysutils.chk_sys_for(i):
                f.write('sudo apt-get install {}; '.format(i))

        # Upgrade pip first
        f.write('pip install --upgrade pip; ')

        # Check for core pip libraries
        for i in pip_installs:
            f.write('pip install {}; '.format(i))

        f.write('which python; ')
        f.write('which pip; ')
        f.write('pip list --format legacy; pip install --upgrade pip')
        f.write('"\n')
        # Check exit code
        f.write('if [ "$?" = "1"  ]; then\n')
        f.write('\techo \"python executable at: \"\n')
        f.write('\twhich python\n')
        f.write('else\n')
        f.write('\texit 1\n')
        f.write('fi\n')
        f.write('\n')


def setup_git(config):
    # Initialize git repo
    cmd = ['git', 'init']
    sysutils.run_in_dir(cmd, config['projectname'])

    # Add user to gitconfig
    filename = config['projectname'] + '/.git/config'

    with open(filename, 'a') as f:
        f.write('\n')
        f.write('[user]\n')
        # User info
        f.write('   name = {}\n'.format(config['author']))
        f.write('   email = {}\n'.format(config['email']))
        f.write('\n')
        # Aliases
        f.write('[alias]\n')
        f.write('   last = log -1 HEAD')


def cp_templates(project_name):
    files = ['.gitignore', '.env', '.konchrc', 'pytest.ini', 'main.py']
    filepath = project_name + '/'

    for f in files:
        shutil.copy(TEMPLATE_DIR + f, filepath + f)

    # Potentially should do a separate directory for source/tests?
    logger = TEMPLATE_DIR + 'logger.py'
    shutil.copy(logger, filepath + 'src/logger.py')


def write_json_config(config):
    # Write the default settings to the project folder
    filepath = config['projectname'] + '/config.json'
    with open(filepath, 'w') as f:
        json.dump(config, f)


def setup_project_env(config):
    project_name = config['projectname']
    # I don't want this to rely on new_project, so we'll ensure the dir too
    ensure_dir(project_name)

    # Setup python 2 virtualenv
    sysutils.new_virtualenv(config['python'], project_name)

    # Upgrade pip
    # Install needed packages:
    #   py.test

    # Setup the setup.sh file - lol, this is getting rediculous.
    make_setup_files(config)

    # Make requirements.txt?


def new_project(config):
    project_name = config['projectname']

    # Create the directory structure
    setup_dirs(project_name)

    # Populate the __init_.py files
    setup_init_files(project_name)

    # Create the README.md
    readme.make_readme(config)

    # Create the LICENSE
    write_license(config)

    # Setup git repo
    setup_git(config)

    # Setup the config files from templates
    cp_templates(project_name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Streamlined Python project scaffolding.")
    args = parser.parse_args()

    config = wizard.wizard()
    print(config)
    print('Starting up project!')
    new_project(config)
    setup_project_env(config)

    # Run the setup file
    cmd = ['sh', 'setup.sh']
    sysutils.run_in_dir(cmd, config['projectname'])

    # Show installed programs summary
    #  sysutils.chk_sys_libraries()
    #  sysutils.chk_pip_libraries(config['python'])

    # Write the project config to json
    write_json_config(config)
