#!/usr/bin/env python
# This file is managed by 'repo_helper'. Don't edit it directly.

# stdlib
import sys

# 3rd party
from setuptools import setup

sys.path.append('.')

# this package
from __pkginfo__ import *  # pylint: disable=wildcard-import

data_files = [('share/applications', ['wxIconSaver.desktop'])]
with open('wxIconSaver.desktop', 'w') as desktop:
	desktop.write(
			f'''[Desktop Entry]
Version={__version__}
Name={modname}
Comment=A GUI utility for saving wxPython icons to files
Exec=wxIconSaver
Icon=document-save
Terminal=false
Type=Application
Categories=Utility;Application;
'''
			)

setup(
		data_files=data_files,
		description='wxPython GUI for saving icons to files.',
		extras_require=extras_require,
		install_requires=install_requires,
		py_modules=[],
		version=__version__,
		)
