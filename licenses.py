def get(license):
    return available.get(license, None)


def format_text(license, name, year=None):
    year = str(current_year())
    return license.format(year=year, name=name) or None


def current_year():
    import datetime as dt
    now = dt.datetime.now()
    return now.year


# These are helpful for tests
MIT_TEXT = 'The MIT License (MIT)'
GNU_TEXT = 'GNU GENERAL PUBLIC LICENSE'

# The MIT License (MIT://opensource.org/licenses/mit-license.php
MIT = """The MIT License (MIT)
Copyright (c) <{year}> <{name}>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

# http://www.gnu.org/licenses/gpl.html
GNU = """GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

one line to give the program's name and an idea of what it does.
Copyright (C) {year}  {name}

This program is free software; you can redistribute it and/or modify it under the terms of the
GNU General Public License as published by the Free Software Foundation; either version 2 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See
the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if
not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301, USA.
"""


GNU_INTERACTIVE = """
Gnomovision version 69, Copyright (C) {year} {name}
Gnomovision comes with ABSOLUTELY NO WARRANTY; for details
type `show w'.  This is free software, and you are welcome
to redistribute it under certain conditions; type `show c'
for details.
"""

available = {
    'MIT': MIT,
    'GNU': GNU,
}
