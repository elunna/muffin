import wizard

"""
Tests for valid_projectname(projectname)
"""


def test_valid_projectname_nospaces():
    t = 'newproject'
    expected = True
    assert wizard.valid_projectname(t) == expected


def test_valid_projectname_spaces():
    t = 'new project'
    expected = False
    assert wizard.valid_projectname(t) == expected


def test_valid_projectname_spacesonends():
    t = ' new_project '
    expected = True
    assert wizard.valid_projectname(t) == expected


"""
Tests for valid_license(license)
"""


def test_validlicense_MIT():
    assert wizard.valid_license('mit')


def test_validlicense_GNU():
    assert wizard.valid_license('GNU')


def test_validlicense_XXX():
    assert wizard.valid_license('XXX') is False
