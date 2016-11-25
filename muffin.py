#!/usr/bin/env python
""" Manages the creation of a new templated Python project. """

import argparse
import json
from .muffin import licenses
import os
from .muffin import readme
import shutil
from .muffin import sysutils
from .muffin import wizard

SUBDIRS = ['src', 'tests', 'data', 'temp', 'logs']
CORE_MODULES = []

PY_MODULES = {
    # We need the security libraries because older versions of py2 don't have good ssl.
    '2.7': ['urllib3[secure]', 'requests[security]'] + CORE_MODULES,
    '3.4': [] + CORE_MODULES,
    '3.5': [] + CORE_MODULES,
}

XTRA_MODULES = ['konch', 'ipython', 'pytest', 'sphinx', 'beautifulsoup4',
                'scrapy', 'requests', 'django', 'selenium']


def wipe_dir(venv):
    """ Clears out the given directory. """
    if os.path.isdir(venv):
        shutil.rmtree(venv)


def ensure_dir(_dir):
    """ Makes sure that the given directory is created and exists. """
    if not os.path.exists(_dir):
        os.makedirs(_dir)


def write_license(conf):
    """ Creates the LICENSE file based on what license the user chose. """
    text = licenses.get(conf['license'])
    filename = conf['projectname'] + '/LICENSE'
    with open(filename, 'w') as f:
        f.write(text)


def make_setup_sh(conf):
    """ Creates the setup.sh file which does the all the pip installs for modules."""
    ensure_dir(conf['projectname'])
    setupfile = conf['projectname'] + '/setup.sh'
    pip_installs = PY_MODULES[conf['python']] + conf.get('modules', [])

    with open(setupfile, 'w') as f:
        f.write("#!/bin/bash\n")
        f.write("# Purpose: Installs the required modules for {}.\n".format(
            conf['projectname']))
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


def setup_git(conf):
    """ Sets up the git repo, the .gitignore file, and makes sure the user's name
        and email are in the .gitconfig.
    """
    ensure_dir(conf['projectname'])
    commands = ['git', 'init']
    sysutils.run_cmd_in_dir(commands, conf['projectname'])

    # Add user to gitconfig
    filename = conf['projectname'] + '/.git/config'

    with open(filename, 'a') as f:
        f.write('\n')
        f.write('[user]\n')
        # User info
        f.write('   name = {}\n'.format(conf['author']))
        f.write('   email = {}\n'.format(conf['email']))
        f.write('\n')
        # Aliases
        f.write('[alias]\n')
        f.write('   last = log -1 HEAD')


def cp_templates(conf):
    """ Copies the designated template from the folder given in the config
        dictionary.
    """
    TEMPLATE_DIR = conf.get('template', None)
    project = conf.get('projectname', None)
    if not project:
        raise Exception('Projectname not set!!!')

    if not TEMPLATE_DIR:
        raise Exception('Template directory not set!!!')

    shutil.copytree(TEMPLATE_DIR, project)


def save_config(conf):
    """ Saves the most recent settings as defaults, so when a user runs muffin.py
        again they can [Enter] through most defaults.
    """
    ensure_dir(conf['projectname'])
    # Write the default settings to the project folder
    filepath = conf['projectname'] + '/config.json'
    with open(filepath, 'w') as f:
        json.dump(conf, f)


def new_venv(conf):
    """ Creates a new virtualenv and creates the setup.sh file to go with it. """
    project_name = conf['projectname']
    ensure_dir(project_name)

    # Setup virtualenv
    sysutils.new_virtualenv(conf['python'], project_name)

    # Setup the setup.sh file
    make_setup_sh(conf)


def new_project(conf):
    """ Runs through all the steps to create a template project. """
    # Setup the project from the template folder
    cp_templates(conf)

    # Create the README.md
    readme.make_readme(conf)

    # Create the LICENSE
    write_license(conf)

    # Setup git repo
    setup_git(conf)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Streamlined Python project scaffolding.")
    args = parser.parse_args()

    config = wizard.wizard()
    print(config)
    print('Starting up project!')
    new_project(config)
    new_venv(config)

    # Run the setup file
    cmd = ['sh', 'setup.sh']
    sysutils.run_cmd_in_dir(cmd, config['projectname'])

    # Show installed programs summary
    #  sysutils.chk_sys_libraries()
    #  sysutils.chk_pip_libraries(config['python'])

    # Write the project config to json
    save_config(config)
