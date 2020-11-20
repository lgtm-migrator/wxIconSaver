#!/usr/bin/env python
# This file is managed by 'repo_helper'. Don't edit it directly.

# stdlib
import sys

# 3rd party
from setuptools import setup

sys.path.append('.')

# stdlib
from textwrap import dedent

# this package
from __pkginfo__ import *  # pylint: disable=wildcard-import

with open("wxIconSaver.desktop", 'w') as desktop:
	desktop.write(
			dedent(
					f"""\
[Desktop Entry]
Version={__version__}
Name=wxIconSaver
Comment=wxPython GUI for saving icons to files.
Exec=wxIconSaver
Icon=document-save
Terminal=False
Type=Application
Categories=Utility;Application;
"""
					)
			)

setup(
		data_files=[("share/applications", ["wxIconSaver.desktop"])],
		description="wxPython GUI for saving icons to files.",
		extras_require=extras_require,
		install_requires=install_requires,
		py_modules=[],
		version=__version__,
		)
