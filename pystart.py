import argparse
import licenses
import os
import readme
import shutil
import sysutils
import wizard

SUBDIRS = ['src', 'tests', 'data', 'temp', 'logs']
#  CORE_MODULES = ['pytest', 'konch', 'ipython']
PY_MODULES = {
    # We need the security libraries because older versions of py2 don't have good ssl.
    '2.7': ['urllib3[secure]', 'requests[security]', 'pytest', 'ipython', 'konch'],
    '3.4': ['pytest', 'ipython', 'konch'],
    '3.5': ['pytest', 'ipython', 'konch']
}

XTRA_MODULES = ['beautifulsoup4', 'scrapy', 'requests', 'sphinx', 'django']


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


def get_date():
    import datetime as dt
    now = dt.datetime.now()
    return str(now.date())


def make_readme(info_dict):
    """
    Creates the README.md file and uses the passed in dictionary to fill in the fields.
    Returns the filepath of the created file.
    """
    filename = info_dict['projectname'] + '/' + 'README.md'
    twitter = info_dict.get('twitter', None)
    email = info_dict.get('email', None)
    date = get_date()
    license = info_dict['license']

    with open(filename, 'w') as f:
        f.write('# Project Name: {}'.format(info_dict['projectname']))
        f.write('\n')
        f.write('> {}'.format(info_dict['description']))
        f.write('\n')
        f.write('\n')

        # Add in standard template here.
        f.write(readme.template)

        f.write('## Meta')
        f.write('\n')
        f.write('##### Author: {}'.format(info_dict['author']))
        f.write('\n')
        f.write('##### Start Date: {}'.format(date))
        f.write('\n')
        if twitter:
            f.write('##### Twitter -- [@{}](https://twitter.com/{})'.format(twitter, twitter))
            f.write('\n')
        if email:
            f.write('##### Email -- {}'.format(email))
            f.write('\n')
        f.write('\n')
        f.write('[![](http://img.shields.io/badge/license-{}-blue.svg)]'.format(license))
        f.write('\n')
        f.write('[{}]: See ``LICENSE`` for full text.'.format(info_dict['license']))
        f.write('\n')

    return filename


def write_license(config):
    text = licenses.get(config['license'])
    filename = config['projectname'] + '/LICENSE'
    with open(filename, 'w') as f:
        f.write(text)


def make_gitignore(project_name):
    """
    Creates the .gitignore file. We'll just copy the one stored away - it should be pretty
    thorough - it's pretty cheap to maintain and saves a lot of future work!
    """
    template = 'gitignore_template.txt'
    filepath = project_name + '/.gitignore'
    shutil.copy(template, filepath)
    return filepath


def make_env(project_name):
    template = 'env_template.txt'
    filepath = project_name + '/.env'
    shutil.copy(template, filepath)
    return filepath


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


def setup_pyfiles(project_name):
    """Setup the main.py, and logger.py modules."""
    main, logger = 'main.py', 'src/logger.py'
    shutil.copy(main, project_name + '/' + main)
    shutil.copy(logger, project_name + '/' + logger)


def setup_project_env(config):
    project_name = config['projectname']
    # I don't want this to rely on new_project, so we'll ensure the dir too
    ensure_dir(project_name)

    # Setup python 2 virtualenv
    sysutils.new_virtualenv(config['python'], project_name)

    # Upgrade pip
    # Install needed packages:
    #   py.test
    #

    # Setup an autoenv file
    make_env(project_name)

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
    make_readme(config)

    # Create the .gitignore
    make_gitignore(project_name)

    # Create the LICENSE
    write_license(config)

    # Create the .py files
    setup_pyfiles(project_name)

    # Setup git repo
    setup_git(config)

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
    sysutils.chk_sys_libraries()
    sysutils.chk_pip_libraries(config['python'])
