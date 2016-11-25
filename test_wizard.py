"""
  " Tests for the wizard module.
  " How to test input_loop?
  " This is an interactive console function. How to test?
  """

import pytest
from . import wizard


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


def test_validlicense_MIT():
    assert wizard.valid_license('mit')


def test_validlicense_GNU():
    assert wizard.valid_license('GNU')


def test_validlicense_XXX():
    assert wizard.valid_license('xxx') is False


def test_validtemplate_invalid_returnsFalse():
    assert wizard.valid_template('somethine') is False


def test_validtemplate_validname_but_dne_returnsFalse():
    assert wizard.valid_template('template_234087adskf') is False


def test_validtemplate_validname_exists_returnsTrue():
    assert wizard.valid_template('templates') is True


def test_yesorno_valid():
    assert wizard.yesorno('n') is True
    assert wizard.yesorno('N') is True
    assert wizard.yesorno('y') is True
    assert wizard.yesorno('Y') is True


def test_yesorno_invalid():
    assert wizard.yesorno('z') is False
    assert wizard.yesorno('') is False
    assert wizard.yesorno(' ') is False


def test_getdefaults_dflt_file_returnsDict():
    result = wizard.get_defaults()
    assert isinstance(result, dict)


def test_getdefaults_fileexists_returnsDict():
    filepath = 'defaults.json'
    result = wizard.get_defaults(filepath)
    assert isinstance(result, dict)


def test_getdefaults_fileDNE_raisesException():
    filepath = 'youarenotpossible.txt'
    with pytest.raises(IOError):
        wizard.get_defaults(filepath)
