import argparse
import licenses
import os
import readme
import shutil
import wizard

SUBDIRS = ['src', 'tests', 'data', 'temp']


def setup_dirs(projectname):
    # Create main project directory
    os.makedirs(projectname)

    for sub in SUBDIRS:
        # Create each subdirectory
        os.makedirs(projectname + '/' + sub)


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


def setup_virtualenv():
    # Setup python 2 virtualenv
    # Upgrade pip
    # Install needed packages:
    #   py.test
    #
    # Setup an autoenv file???
    # requirements.txt
    pass


def setup_git():
    # Initialize git repo
    # Create thorough .gitignore
    pass


# Create a main.py run file
def setup_main():
    # Setup logger
    # Setup argparse, basic.
    # Create main run func
    pass


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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Streamlined Python project scaffolding.")
    args = parser.parse_args()

    config = wizard.wizard()
    print(config)
    new_project(config)
