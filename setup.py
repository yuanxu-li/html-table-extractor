#!/usr/bin/python
# -*- coding: utf-8 -*-

"""A tool to extract data from html table

See:
https://github.com/yuanxu-li/table-extractor
"""

import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='table-extractor',
    url='https://github.com/yuanxu-li/table-extractor',
    version='1.0.0',
    author='Justin Li',
    author_email='yuanxu.lee@gmail.com',
    description='A python library for extracting data from html table',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='html table beautifulsoup crawler scrape',
    packages=[
        'table_extractor',
    ]
    install_requires=[
        'beautifulsoup4==4.5.3',
    ],
    long_description=long_description,
)