from string import ascii_letters
from licenses import available
import json


def input_loop(prompt, required=True, validator=None, default=None):
    while True:
        # Show the remembered default (if we have one)
        if default:
            val = raw_input('{}[{}]:> '.format(prompt, default))
        else:
            val = raw_input('{}:> '.format(prompt))

        # If we have a default, make it easy for the user to press enter and accept it.
        if val == '' and default:
            return default
        elif not val and required:
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


def get_defaults():
    # Read JSON defaults
    DFLT_FILE = 'defaults.json'
    with open(DFLT_FILE, 'r') as f:
        contents = f.read()
        defaults = json.loads(contents)
    return defaults


def wizard():
    """
    Collects project info and returns a dict.
    """
    dflts = get_defaults()
    wiz_dict = {}

    # input_loop(prompt, req=True, validator=None, choices=None, default=None):
    # Ask for project name
    wiz_dict['projectname'] = input_loop('Project name',
                                         validator=valid_projectname)

    # Ask for author
    wiz_dict['author'] = input_loop('Author', default=dflts.get('author', None))

    # Ask for project purpose
    wiz_dict['purpose'] = input_loop('Short summary', required=False)

    # Ask for license
    wiz_dict['license'] = input_loop('License type',
                                     validator=valid_license,
                                     default=dflts.get('license', None))

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
