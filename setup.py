from __future__ import absolute_import
import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "coawst_regress",
    version = "0.0.1",
    author = "blah",
    author_email = "blah@gmail.com",
    description = ("Sample repository to learn to sprint on open source "
                   "software"),
    license = "BSD",
    keywords = "example sprint tutorial",
    url = "https://github.com/blah",
    long_description=read('README.md'),
    packages=find_packages(),
    package_data={'': ['testcases/*.*']},
)