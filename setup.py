# -*- coding: utf-8 -*-
""" 
Project : PyCoA-CoaData
Date :    january 2021
Authors : Olivier Dadoun, Julien Browaeys, Tristan Beau
Copyright ©pycoa.fr

About : mandatory setup file
"""

from setuptools import setup, find_packages

pkg_vars  = {}
with open("coacache/_version.py") as fp:
    exec(fp.read(), pkg_vars)

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='CoaData',
    url='https://github.com/coa-project/coadata',
    version=pkg_vars['__version__'],
    author=pkg_vars['__author__'],
    author_email=pkg_vars['__email__'],
    # Needed to actually package something
    packages=['coacache'],
    # Needed for dependencies
    # The license can be anything you like
    license='MIT',
    description='PyCoA stands for Python COvid19 Analysis project, which is an open source project initially designed to run in the Google colab environment. See pycoa.fr website.',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.md').read(),
)
