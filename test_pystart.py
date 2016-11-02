import os
import shutil
import pystart
import pytest
"""
Tests for setup_dirs()
"""
TEST_PROJ = 'testproject'
MIT_CONFIG = {
    'projectname': TEST_PROJ,
    'author': 'lunatunez',
    'purpose': 'Short blurb',
    'license': 'MIT'
}

GNU_CONFIG = {
    'projectname': TEST_PROJ,
    'author': 'lunatunez',
    'purpose': 'Short blurb',
    'license': 'GNU'
}


def wipe_project():
    if os.path.isdir(TEST_PROJ):
        shutil.rmtree(TEST_PROJ)


@pytest.yield_fixture(autouse=True)
def cleanup():
    wipe_project()
    yield None
    wipe_project()

"""
Tests for setup_dirs(projectname)
"""


def test_setupdirs_makes_project_dir():
    pystart.setup_dirs(TEST_PROJ)
    assert os.path.isdir(TEST_PROJ)  # Error making project dir


def test_setupdirs_subdirs():
    # Uses a test generator to go through all the subdirectories we want to test.
    for i in pystart.SUBDIRS:
        subdir = TEST_PROJ + '/' + i
        yield check_dir, subdir


def check_dir(d):
    # This has to go here bc cleanup get called before and after this method.
    pystart.setup_dirs(TEST_PROJ)
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
    pystart.setup_dirs(TEST_PROJ)
    pystart.setup_init_files(TEST_PROJ)
    assert os.path.exists(filename)  # Filename doesn't exist


"""
Tests for make_readme(info_dict)
"""


def readme_factory(**params):
    pystart.setup_dirs(TEST_PROJ)
    config = MIT_CONFIG
    if params:
        config.update(params)

    return pystart.make_readme(config)


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
    pystart.setup_dirs(TEST_PROJ)
    lic_path = TEST_PROJ + '/LICENSE'
    pystart.write_license(MIT_CONFIG)
    assert os.path.exists(lic_path)  # LICENSE file doesn't exist


def test_writelicense_GNU():
    pystart.setup_dirs(TEST_PROJ)
    lic_path = TEST_PROJ + '/LICENSE'
    pystart.write_license(GNU_CONFIG)
    assert os.path.exists(lic_path)  # LICENSE file doesn't exist

"""
Tests for make_gitignore(info_dict)
"""


def test_makegitignore_exists():
    pystart.setup_dirs(TEST_PROJ)
    # Verify that make_readme returns the filepath
    f = pystart.make_gitignore(TEST_PROJ)
    assert os.path.exists(f)  # .gitignore was not created in project/


def test_makegitignore_essentialfiles():
    pystart.setup_dirs(TEST_PROJ)
    filepath = pystart.make_gitignore(TEST_PROJ)
    with open(filepath, 'r') as f:
        lines = f.read().splitlines()
    assert '*.pyc' in lines
    assert '*.log' in lines
    assert 'db.sqlite3' in lines


def test_makegitignore_essentialdirectories():
    pystart.setup_dirs(TEST_PROJ)
    filepath = pystart.make_gitignore(TEST_PROJ)
    with open(filepath, 'r') as f:
        lines = f.read().splitlines()
    assert '__pycache__/*' in lines
    assert '.ropeproject/*' in lines
    assert 'venv/*' in lines
    assert 'data/*' in lines
    assert 'tests/*' in lines
