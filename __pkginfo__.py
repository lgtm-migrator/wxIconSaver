# Copyright (C) 2019 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

# This script based on https://github.com/rocky/python-uncompyle6/blob/master/__pkginfo__.py

copyright   = """
2019 Dominic Davis-Foster <dominic@davis-foster.co.uk>
"""

classifiers =  ['Development Status :: 3 - Alpha',
				'Intended Audience :: Developers',
				'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
				'Operating System :: OS Independent',
				'Programming Language :: Python',
				'Programming Language :: Python :: 3.6',
				'Programming Language :: Python :: 3.7',
				'Programming Language :: Python :: 3.8',
				]

# TODO: add tag for GUI

# The rest in alphabetic order
author             = "Dominic Davis-Foster"
author_email       = "dominic@davis-foster.co.uk"
entry_points       = {
	'console_scripts': [
		'wxIconSaver=wxIconSaver:main',
	]}
ftp_url            = None
install_requires   = []

license            = 'GPL3'
modname            = "wxIconSaver"
py_modules         = ['wxIconSaver']
short_desc         = 'wxPython GUI for saving icons to files'
web                = 'https://github.com/domdfcoding/wxIconSaver'


import os.path
def get_srcdir():
	filename = os.path.normcase(os.path.dirname(os.path.abspath(__file__)))
	return os.path.realpath(filename)

srcdir = get_srcdir()

def read(*rnames):
	return open(os.path.join(srcdir, *rnames)).read()

# Get info from files; set: long_description and VERSION
long_description   = ( read("README.rst") + '\n' )
exec(read('version.py'))