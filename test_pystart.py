import licenses
import os
import shutil
import pystart
import pytest
"""
Tests for setup_dirs()
"""
TEST_PROJ = 'testproject'


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
    f = TEST_PROJ + '/' + 'README.md'
    proj = {
        'name': TEST_PROJ,
        'author': 'lunatunez',
        'start': '2016-01-01',
        'end': '2017-01-01',
        'purpose': 'Test',
        'license': 'MIT'
    }
    if params:
        proj.update(params)

    pystart.make_readme(proj)
    return f


def test_makereadme_empty():
    f = readme_factory()
    print(f)
    assert os.path.exists(f)  # README.md was not created in project/


def test_makereadme_author():
    readme = readme_factory()
    t = "Author: lunatunez"
    with open(readme, 'r') as f:
        assert t in f.read().splitlines()  # Check if Author field is in README


def test_makereadme_projectname():
    readme = readme_factory()
    t = "Project Name: testproject"
    with open(readme, 'r') as f:
        assert t in f.read().splitlines()  # Check if Project Name field is in README


def test_makereadme_purpose():
    readme = readme_factory()
    t = "Purpose: Test"
    with open(readme, 'r') as f:
        assert t in f.read().splitlines()  # Check if Purpose field is in README


def test_makereadme_startdate():
    readme = readme_factory()
    t = "Start Date: 2016-01-01"
    with open(readme, 'r') as f:
        assert t in f.read().splitlines()  # Check if Start Date field is in README


def test_makereadme_enddate():
    readme = readme_factory()
    t = "End Date: 2017-01-01"
    with open(readme, 'r') as f:
        assert t in f.read().splitlines()  # Check if End Date field is in README
        #  assert any(l.strip() == t for l in f.readlines())  # Check if End Date field is in README


def test_makereadme_mit_licence():
    readme = readme_factory(license='MIT')
    expected = licenses.MIT_TEXT
    with open(readme, 'r') as f:
        assert any(l.strip() == expected for l in f.readlines())  # Check if MIT Licence is in README


def test_makereadme_gnu_licence():
    readme = readme_factory(license='GNU')
    expected = licenses.GNU_TEXT
    with open(readme, 'r') as f:
        assert any(l.strip() == expected for l in f.readlines())  # Check if MIT Licence is in README
