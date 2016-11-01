import licenses

"""
Tests for get(license):
"""


def test_get_MIT():
    expected = 'The MIT License (MIT)'
    #  firstline = licenses.get('MIT')[0].strip()
    firstline = licenses.get('MIT').split('\n')[0]
    assert firstline == expected


def test_get_GNU():
    expected = 'GNU GENERAL PUBLIC LICENSE'
    #  firstline = licenses.get('GNU')[0].strip()
    firstline = licenses.get('GNU').split('\n')[0]
    assert firstline == expected


def test_get_INVALID():
    expected = None
    firstline = licenses.get('INVALID')
    assert firstline is expected

"""
Tests for format_license(key, name, date)
"""
