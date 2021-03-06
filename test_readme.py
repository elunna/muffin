""" Tests for the readme module. """

from . import muffin
import os
import pytest
from . import readme
from . import test_configs


@pytest.yield_fixture(autouse=True)
def cleanup():
    muffin.wipe_dir(test_configs.TEST_PROJ)
    yield None
    muffin.wipe_dir(test_configs.TEST_PROJ)


def readme_factory(**params):
    muffin.ensure_dir(test_configs.TEST_PROJ)
    # Just create the directory
    config = test_configs.FULL_CONFIG
    if params:
        config.update(params)

    return readme.make_readme(config)


def test_makereadme_empty():
    # Verify that make_readme returns the filepath
    f = readme_factory()
    assert os.path.exists(f)  # README.md was not created in project/


def test_makereadme_author():
    README = readme_factory()
    t = "##### Author: lunatunez"
    with open(README, 'r') as f:
        assert t in f.read().splitlines()  # Check if Author field is in README


def test_makereadme_title_header():
    README = readme_factory()
    t = "# Project Name: testproject"
    with open(README, 'r') as f:
        assert t in f.read().splitlines()  # Check if Project Name field is in README


def test_makereadme_blurb():
    README = readme_factory()
    t = "> Short blurb"
    with open(README, 'r') as f:
        assert t in f.read().splitlines()  # Check if Project Name field is in README


def test_makereadme_email():
    README = readme_factory(email='rdash@cloudsdale.net')
    t = '##### Email -- rdash@cloudsdale.net'
    with open(README, 'r') as f:
        assert t in f.read().splitlines()  # Check if Project Name field is in README


def test_makereadme_twitter():
    README = readme_factory(twitter='rdashie')
    t = '##### Twitter -- [@rdashie](https://twitter.com/rdashie)'
    with open(README, 'r') as f:
        assert t in f.read().splitlines()  # Check if Project Name field is in README


def test_makereadme_mit_license():
    README = readme_factory(license='MIT')
    expected = '[![](http://img.shields.io/badge/license-MIT-blue.svg)]'
    with open(README, 'r') as f:
        # Check if MIT Licence is in README
        assert any(l.strip() == expected for l in f.readlines())


def test_makereadme_gnu_license():
    README = readme_factory(license='GNU')
    expected = '[![](http://img.shields.io/badge/license-GNU-blue.svg)]'
    with open(README, 'r') as f:
        # Check if MIT Licence is in README
        assert any(l.strip() == expected for l in f.readlines())
