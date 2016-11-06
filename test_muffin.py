import os
from muffin import *
import pytest

"""
Tests for setup_dirs()
"""
TEST_PROJ = 'testproject'
MIT_CONFIG = {
    'projectname': TEST_PROJ,
    'author': 'lunatunez',
    'description': 'Short blurb',
    'license': 'MIT',
    'email': 'rdash@cloudsdale.net',
    'twitter': 'rdashie',
}

GNU_CONFIG = {
    'projectname': TEST_PROJ,
    'author': 'lunatunez',
    'description': 'Short blurb',
    'license': 'GNU',
    'email': 'rdash@cloudsdale.net',
    'twitter': 'rdashie',
}

VENV_CONFIG = {
    'projectname': TEST_PROJ,
    'author': 'lunatunez',
    'description': 'Short blurb',
    'license': 'GNU',
    'python': '2.7',
    'email': 'rdash@cloudsdale.net',
    'twitter': 'rdashie',
}

VENV_CONFIG_PKGS = {
    'projectname': TEST_PROJ,
    'author': 'lunatunez',
    'description': 'Short blurb',
    'license': 'GNU',
    'python': '2.7',
    'packages': ['pytest', 'autoenv', 'konch', 'pip', 'pandas']
}


@pytest.yield_fixture(autouse=True)
def cleanup():
    wipe_dir(TEST_PROJ)
    yield None
    wipe_dir(TEST_PROJ)

"""
Tests for setup_dirs(projectname)
"""


def test_setupdirs_makes_project_dir():
    setup_dirs(TEST_PROJ)
    assert os.path.isdir(TEST_PROJ)  # Error making project dir


def test_setupdirs_subdirs():
    # Uses a test generator to go through all the subdirectories we want to test.
    for i in SUBDIRS:
        subdir = TEST_PROJ + '/' + i
        yield check_dir, subdir


def check_dir(d):
    # This has to go here bc cleanup get called before and after this method.
    setup_dirs(TEST_PROJ)
    assert os.path.isdir(d)  # Directory doesn't exist

"""
Tests for setup_init_files(projectname)
"""


def test_setupinitfiles():
    init_files = ['/', '/src', '/tests']

    # Uses a test generator to go through all the init files we want to test.
    for i in init_files:
        init = TEST_PROJ + i + '/__init__.py'
        yield check_init_file, init


def check_init_file(filename):
    setup_dirs(TEST_PROJ)
    setup_init_files(TEST_PROJ)
    assert os.path.exists(filename)  # Filename doesn't exist


"""
Tests for make_readme(info_dict)
"""


def readme_factory(**params):
    setup_dirs(TEST_PROJ)
    config = MIT_CONFIG
    if params:
        config.update(params)

    return make_readme(config)


def test_makereadme_empty():
    # Verify that make_readme returns the filepath
    f = readme_factory()
    assert os.path.exists(f)  # README.md was not created in project/


def test_makereadme_author():
    readme = readme_factory()
    t = "##### Author: lunatunez"
    with open(readme, 'r') as f:
        assert t in f.read().splitlines()  # Check if Author field is in README


def test_makereadme_title_header():
    readme = readme_factory()
    t = "# Project Name: testproject"
    with open(readme, 'r') as f:
        assert t in f.read().splitlines()  # Check if Project Name field is in README


def test_makereadme_blurb():
    readme = readme_factory()
    t = "> Short blurb"
    with open(readme, 'r') as f:
        assert t in f.read().splitlines()  # Check if Project Name field is in README


def test_makereadme_email():
    readme = readme_factory(email='rdash@cloudsdale.net')
    t = '##### Email -- rdash@cloudsdale.net'
    with open(readme, 'r') as f:
        assert t in f.read().splitlines()  # Check if Project Name field is in README


def test_makereadme_twitter():
    readme = readme_factory(twitter='rdashie')
    t = '##### Twitter -- [@rdashie](https://twitter.com/rdashie)'
    with open(readme, 'r') as f:
        assert t in f.read().splitlines()  # Check if Project Name field is in README


def test_makereadme_mit_license():
    readme = readme_factory(license='MIT')
    expected = '[![](http://img.shields.io/badge/license-MIT-blue.svg)]'
    with open(readme, 'r') as f:
        assert any(l.strip() == expected for l in f.readlines())  # Check if MIT Licence is in README


def test_makereadme_gnu_license():
    readme = readme_factory(license='GNU')
    expected = '[![](http://img.shields.io/badge/license-GNU-blue.svg)]'
    with open(readme, 'r') as f:
        assert any(l.strip() == expected for l in f.readlines())  # Check if MIT Licence is in README

"""
Tests for write_license(config)
"""


def test_writelicense_MIT():
    setup_dirs(TEST_PROJ)
    lic_path = TEST_PROJ + '/LICENSE'
    write_license(MIT_CONFIG)
    assert os.path.exists(lic_path)  # LICENSE file doesn't exist


def test_writelicense_GNU():
    setup_dirs(TEST_PROJ)
    lic_path = TEST_PROJ + '/LICENSE'
    write_license(GNU_CONFIG)
    assert os.path.exists(lic_path)  # LICENSE file doesn't exist

"""
Tests for make_gitignore(info_dict)
"""


def test_makegitignore_exists():
    setup_dirs(TEST_PROJ)
    # Verify that make_readme returns the filepath
    f = make_gitignore(TEST_PROJ)
    assert os.path.exists(f)  # .gitignore was not created in project/


def test_makegitignore_essentialfiles():
    setup_dirs(TEST_PROJ)
    filepath = make_gitignore(TEST_PROJ)
    with open(filepath, 'r') as f:
        lines = f.read().splitlines()
    assert '*.pyc' in lines
    assert '*.log' in lines
    assert 'db.sqlite3' in lines


def test_makegitignore_essentialdirectories():
    setup_dirs(TEST_PROJ)
    filepath = make_gitignore(TEST_PROJ)
    with open(filepath, 'r') as f:
        lines = f.read().splitlines()
    assert '__pycache__/*' in lines
    assert '.ropeproject/*' in lines
    assert 'venv/*' in lines
    assert 'data/*' in lines
    assert 'tests/*' in lines


"""
Tests for setup_pyfiles(project_name)
"""


def test_setuppyfiles():
    setup_dirs(TEST_PROJ)
    setup_pyfiles(TEST_PROJ)
    assert os.path.exists(TEST_PROJ + '/main.py')  # Error making main.py
    assert os.path.exists(TEST_PROJ + '/src/logger.py')  # Error making utils.py
