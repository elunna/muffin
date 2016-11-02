import licenses
import os
import shutil


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


def make_readme(info_dict):
    """
    Creates the README.md file and uses the passed in dictionary to fill in the fields.
    Returns the filepath of the created file.
    """
    filename = info_dict['projectname'] + '/' + 'README.md'
    twitter_handle = 'rainbowdash'
    email = 'rdash@cloudsdale.net'
    year = 2017
    license = licenses.get(info_dict['license'])

    with open(filename, 'w') as f:
        f.write('# Project Name: {}'.format(info_dict['projectname']))
        f.write('\n')
        f.write('> {}'.format(info_dict['purpose']))
        f.write('\n')
        f.write('\n')

        # Add in standard template here.

        f.write('## Meta')
        f.write('\n')
        f.write('Author: {}'.format(info_dict['author']))
        f.write('\n')
        #  f.write('Start Date: {}'.format(info_dict['start']))
        f.write('\n')
        f.write('Socials :wavy_dash: [@{}](https://twitter.com/{}) :wavy_dash: {}'.format(
            twitter_handle, twitter_handle, email))
        f.write('\n')
        f.write('### Licence [![](http://img.shields.io/badge/license-{}-blue.svg)][license]'.format(
            info_dict['license']))
        f.write('\n')
        f.write('XYZ license. See ``LICENSE.txt`` for full text.'.format(info_dict['license']))
        f.write('\n')

        if license:
            license_txt = licenses.format_text(license, name=info_dict['projectname'], year=year)
            f.write(license_txt)

        f.write('<p align="right"><a href="#top">:arrow_up:</a></p>')

    return filename


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


def get_date():
    # Returns todays date
    pass


def user_prompt(prompt):
    input = raw_input('{}:> '.format(prompt))
    return input


def wizard():
    """
    Collects project info and returns a dict.
    """
    wiz_dict = {}

    # Ask for project name
    wiz_dict['projectname'] = user_prompt('Project name')

    # Ask for author
    wiz_dict['name'] = user_prompt('Author')

    # Ask for project purpose
    wiz_dict['purpose'] = user_prompt('Short project description')

    # Create functional tests for
        # py-test
        # logger

    # Ask for starting modules
        # For each module, ask for starting functions and create tests for each

    # Ask if we want Beautiful Soup and request
        # Functional test
    # Ask if we want scrapy
        # Functional test
    return wiz_dict


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


if __name__ == "__main__":
    config = wizard()
    print(config)
