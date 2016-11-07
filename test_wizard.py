import wizard

# Tests for input_loop
# This is an interactive console function. How to test?

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
    expected = False
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


"""
Tests for valid_template(template)
"""


def test_validtemplate_invalid_returnsFalse():
    assert wizard.valid_template('somethine') is False


def test_validtemplate_validname_but_dne_returnsFalse():
    assert wizard.valid_template('template_234087adskf') is False


def test_validtemplate_validname_exists_returnsTrue():
    assert wizard.valid_template('templates') is True


"""
Tests for yesorno(choice)
"""


def test_yesorno_valid():
    assert wizard.yesorno('n') is True
    assert wizard.yesorno('N') is True
    assert wizard.yesorno('y') is True
    assert wizard.yesorno('Y') is True


def test_yesorno_invalid():
    assert wizard.yesorno('z') is False
    assert wizard.yesorno('') is False
    assert wizard.yesorno(' ') is False
