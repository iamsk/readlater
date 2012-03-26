#!/usr/bin/env python
#-*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

name = "readlater"
version = "0.1"

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name=name,
    version=version,
    description="类 read it later 应用之间的数据交换",
    long_description=read('README.md'),
    keywords="",
    author="",
    author_email='',
    url='https://bitbucket.org/iamsk/readlater',
    license='',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'readability-api',
        'ril'
        ],
    entry_points="""
    [console_scripts]
    start = readlater.export_import:run
    """,
)
