from string import ascii_letters


def user_prompt(prompt):
    while True:
        input = raw_input('{}:> '.format(prompt))
    return input


def valid_projectname(projectname):
    # Can only contain alphabetic characters or underscores.
    n = projectname.strip()
    if ' ' in n:
        return False
    else:
        return any(c in ascii_letters + '_' for c in n)


def valid_license(license):
    pass


def wizard():
    """
    Collects project info and returns a dict.
    """
    wiz_dict = {}

    # Ask for project name
    wiz_dict['projectname'] = user_prompt('Project name')

    # Ask for author
    wiz_dict['author'] = user_prompt('Author')

    # Ask for project purpose
    wiz_dict['purpose'] = user_prompt('Short project description')

    # Ask for license
    wiz_dict['license'] = user_prompt('License type')

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
