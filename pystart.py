import os


def setup_dirs(projectname):
    # Create main project directory
    os.makedirs(projectname)

    # Create main/src
    # Create main/tests
    # Create main/data
    # Create main/temp
    pass


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


def setup_README():
    # Add info from wizard
    # Add licence info
    pass


def check_existing():
    # Checks if the project folder exists already
    pass


def wizard():
    # Ask for author
    # Ask for project name
    # Ask for project purpose
    # Ask for Start date
    # Ask for end date
    # Create functional tests for
        # py-test
        # logger
        #
    # Ask for starting modules
        # For each module, ask for starting functions and create tests for each

    # Ask if we want Beautiful Soup and request
        # Functional test
    # Ask if we want scrapy
        # Functional test
    pass
