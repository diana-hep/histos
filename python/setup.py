#!/usr/bin/env python

# BSD 3-Clause License; see https://github.com/scikit-hep/aghast/blob/master/LICENSE

import os.path

from setuptools import find_packages
from setuptools import setup


def get_version():
    g = {}
    exec(open(os.path.join("aghast", "version.py")).read(), g)
    return g["__version__"]


def get_description():
    return open("README.md").read()


setup(
    name="aghast",
    version=get_version(),
    packages=find_packages(exclude=["tests"]),
    scripts=[],
    data_files=[],
    description="Aghast: aggregated, histogram-like statistics, sharable as Flatbuffers.",
    long_description=get_description(),
    long_description_content_type="text/markdown",
    author="Jim Pivarski (IRIS-HEP)",
    author_email="pivarski@princeton.edu",
    maintainer="Jim Pivarski (IRIS-HEP)",
    maintainer_email="pivarski@princeton.edu",
    url="https://github.com/scikit-hep/aghast",
    download_url="https://github.com/scikit-hep/aghast/releases",
    license="BSD 3-clause",
    test_suite="tests",
    install_requires=["flatbuffers>=1.8.0", "numpy"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    classifiers=[
        # "Development Status :: 1 - Planning",
        # "Development Status :: 2 - Pre-Alpha",
        # "Development Status :: 3 - Alpha",
        "Development Status :: 4 - Beta",
        # "Development Status :: 5 - Production/Stable",
        # "Development Status :: 6 - Mature",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development",
        "Topic :: Utilities",
    ],
    platforms="Any",
)
