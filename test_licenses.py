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
Tests for format_text(license, name, date=None):
"""


def test_formattext_MIT():
    license = licenses.get('MIT')
    name = 'lunatunez'
    date = '2016'
    expected = 'Copyright (c) <2016> <lunatunez>'
    result = licenses.format_text(license, year=date, name=name)
    # Result is on MIT line 1
    line1 = result.split('\n')[1]
    assert expected == line1


def test_formattext_GNU():
    license = licenses.get('GNU')
    name = 'lunatunez'
    date = '2016'
    expected = 'Copyright (C) 2016  lunatunez'
    result = licenses.format_text(license, year=date, name=name)
    # Result is on GNU line 4
    line4 = result.split('\n')[4]
    assert expected == line4
