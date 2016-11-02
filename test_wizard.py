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
    t = ' new project '
    expected = True
    assert wizard.valid_projectname(t) == expected
