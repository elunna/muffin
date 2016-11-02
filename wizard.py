from string import ascii_letters
from licenses import available


def input_loop(prompt, required=True, validator=None, default=None):
    while True:
        # Show the remembered default (if we have one)
        if default:
            val = raw_input('{}[{}]:> '.format(prompt, default))
        else:
            val = raw_input('{}:> '.format(prompt))

        # If we have a default, make it easy for the user to press enter and accept it.
        if val is None and default:
            return default
        elif val is None and required:
            print('A value is required.')
            print('')
            continue
        elif validator:
            # This value type has a special validator
            if validator(val):
                return val
            else:
                print('')
        else:
            return val


def valid_projectname(projectname):
    # Can only contain alphabetic characters or underscores.
    n = projectname
    if ' ' in n:
        print('Project name cannot contain spaces.')
        return False
    elif all(c in ascii_letters + '_' for c in n):
        return True
    else:
        print('Project name can only contain letters(a-z, A-Z, and underscores(_)')


def valid_license(license):
    result = license.strip().upper() in available
    if result:
        return True
    else:
        print('License must be one of: {}'.format(available))
        return False


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
    wiz_dict['purpose'] = input_loop('Short project description', required=False)

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
