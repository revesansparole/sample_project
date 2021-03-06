#!/usr/bin/env python
# -*- coding: utf-8 -*-

# {{pkglts pysetup.kwds,
# format setup arguments
from os import walk
from os.path import abspath, normpath
from os.path import join as pj
from setuptools import setup, find_packages


short_descr = "belle petite description"
readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')


def parse_requirements(fname):
    with open(fname, 'r') as f:
        txt = f.read()

    reqs = []
    for line in txt.splitlines():
        line = line.strip()
        if len(line) > 0 and not line.startswith("#"):
            reqs.append(line)

    return reqs

# find version number in /src/$pkg_pth/version.py
version = {}
with open("src/sample_project/version.py") as fp:
    exec(fp.read(), version)



setup_kwds = dict(
    name='sample_project',
    version=version["__version__"],
    description=short_descr,
    long_description=readme + '\n\n' + history,
    author="revesansparole",
    author_email='moi@email.com',
    url='',
    license="cecill-c",
    zip_safe=False,

    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=parse_requirements("requirements.txt"),
    tests_require=parse_requirements("dvlpt_requirements.txt"),
    entry_points={},
    keywords='',
    test_suite='nose.collector',
)
# }}
# change setup_kwds below before the next pkglts tag

setup_kwds['entry_points']['console_scripts'] = ['toto = sample_project.cli:main']

# do not change things below
# {{pkglts pysetup.call,
setup(**setup_kwds)
# }}
