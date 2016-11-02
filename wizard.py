from string import ascii_letters
from licenses import available


def user_prompt(prompt):
    return raw_input('{}:> '.format(prompt))


def valid_projectname(projectname):
    # Can only contain alphabetic characters or underscores.
    n = projectname.strip()
    if ' ' in n:
        return False
    else:
        return any(c in ascii_letters + '_' for c in n)


def valid_license(license):
    return license.strip().upper() in available


def wizard():
    """
    Collects project info and returns a dict.
    """
    wiz_dict = {}

    # input_loop(prompt, req=True, validator=None, choices=None, default=None):
    # Ask for project name
    wiz_dict['projectname'] = input_loop('Project name', validator=valid_projectname)

    # Ask for author
    wiz_dict['author'] = input_loop('Author')

    # Ask for project purpose
    wiz_dict['purpose'] = input_loop('Short project description', req=False)

    # Ask for license
    wiz_dict['license'] = input_loop('License type', validator=valid_license)

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
