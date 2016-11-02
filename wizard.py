from string import ascii_letters
from licenses import available
import json
import os

DFLT_FILE = 'defaults.json'


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
    elif not all(c in ascii_letters + '_' for c in n):
        print('Project name can only contain letters(a-z, A-Z, and underscores(_)')
        return False
    elif os.path.isdir(projectname):
        print('Project folder already exists with that name!')
        return False
    else:
        return True


def valid_license(license):
    result = license.strip().upper() in available
    if result:
        return True
    else:
        print('License must be one of: {}'.format(available))
        return False


def get_defaults():
    # Read JSON defaults
    with open(DFLT_FILE, 'r') as f:
        contents = f.read()
        defaults = json.loads(contents)
    return defaults


def update_defaults(dflt_dict, wiz_dict):
    # Update only the fields in the json defaults, and only write if they changed.
    keys = dflt_dict.keys()
    update = False
    for k in keys:
        if dflt_dict.get(k, None) != wiz_dict.get(k, None):
            update = True
            # wiz_dict has a diff val, so we'll update it.
            dflt_dict[k] = wiz_dict.get(k, None)

    if update:
        # Write the new default settings
        with open(DFLT_FILE, 'w') as f:
            json.dump(dflt_dict, f)


def wizard():
    """
    Collects project info and returns a dict.
    """
    dflt_dict = get_defaults()
    wiz_dict = {}

    # input_loop(prompt, req=True, validator=None, choices=None, default=None):
    # Ask for project name
    wiz_dict['projectname'] = input_loop('Project name',
                                         validator=valid_projectname)

    # Ask for author
    wiz_dict['author'] = input_loop('Author', default=dflt_dict.get('author', None))

    # Ask for project purpose
    wiz_dict['purpose'] = input_loop('Short summary', required=False)

    # Ask for license
    wiz_dict['license'] = input_loop('License type',
                                     validator=valid_license,
                                     default=dflt_dict.get('license', None))

    # Ask for project purpose
    wiz_dict['email'] = input_loop('Email', required=False,
                                   default=dflt_dict.get('email', None))

    # Ask for project purpose
    wiz_dict['twitter'] = input_loop('Twitter', required=False,
                                     default=dflt_dict.get('twitter', None))
    # Create functional tests for
        # py-test
        # logger

    # Ask for starting modules
        # For each module, ask for starting functions and create tests for each

    # Ask if we want Beautiful Soup and request
        # Functional test
    # Ask if we want scrapy
        # Functional test

    # Update defaults
    update_defaults(dflt_dict, wiz_dict)

    return wiz_dict
