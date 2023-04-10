#!/usr/bin/env python

import re

from setuptools import setup

with open("jsonpatch.py") as srcfile:
    src = srcfile.read()
    metadata = dict(re.findall('__([a-z]+)__ = "([^"]+)"', src))
    docstrings = re.findall('"""([^"]*)"""', src, re.MULTILINE | re.DOTALL)
    print(metadata)


PACKAGE = "jsonpatch"

MODULES = ["jsonpatch"]

REQUIREMENTS = list(open("requirements.in"))

OPTIONS = {"install_requires": REQUIREMENTS}

AUTHOR_EMAIL = metadata["author"]
VERSION = metadata["version"]
WEBSITE = metadata["website"]
LICENSE = metadata["license"]
DESCRIPTION = docstrings[0]

# Extract name and e-mail ("Firstname Lastname <mail@example.org>")
if mo := re.match(r"(.*) <(.*)>", AUTHOR_EMAIL):
    AUTHOR, EMAIL = mo.groups()
else:
    raise ValueError("Need email in 'name <email>' format")

with open("README.md") as readme:
    README = readme.read()

CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
]


setup(
    name=PACKAGE,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    author=AUTHOR,
    author_email=EMAIL,
    license=LICENSE,
    url=WEBSITE,
    py_modules=MODULES,
    package_data={"": ["requirements.txt"]},
    scripts=["bin/jsondiff", "bin/jsonpatch"],
    classifiers=CLASSIFIERS,
    python_requires=">=3.7",
    project_urls={
        "Website": "https://github.com/stefankoegl/python-json-patch",
        "Repository": "https://github.com/stefankoegl/python-json-patch.git",
        "Documentation": "https://python-json-patch.readthedocs.org/",
        "PyPI": "https://pypi.org/pypi/jsonpatch",
        "Tests": "https://travis-ci.org/stefankoegl/python-json-patch",
        "Test Coverage": "https://coveralls.io/r/stefankoegl/python-json-patch",
    },
    **OPTIONS,  # type: ignore [arg-type]
)
