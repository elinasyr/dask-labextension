#!/usr/bin/env python
# coding: utf-8

# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.

import os
import sys
from distutils.core import setup


class NodeModulesMissing(Exception):
    "raised when node_modules directory is not found"
    pass


if 'develop' in sys.argv or any(a.startswith('bdist') for a in sys.argv):
    import setuptools

# Ensure that js has been built. This does not guaruntee that the packages
# are update to date. In the future we might do a more expensive check
# involving file hashes, but only on sdist and bdist builds.
if not os.path.exists('node_modules'):
    raise NodeModulesMissing("Before Python package can be installed or built, "
                             "JavaScript components must be built using npm. "
                             "Run the following and then retry: "
                             "\nnpm install")

setup_args = dict(
    name                 = 'dask-labextension',
    packages             = ['dask_labextension'],
    version              = '0.0.2',
    author               = 'Luke Canavan and Brian Granger',
    author_email         = 'canavandl@gmail.com and ellisonbg@gmail.com',
    keywords             = ['jupyterlab', 'jupyterlab extension', 'dask'],
    install_requires     = ['jupyterlab>=0.7.0'],
    include_package_data = True
)

if __name__ == '__main__':
    setup(**setup_args)

























from __future__ import print_function

#-----------------------------------------------------------------------------
# Minimal Python version sanity check
#-----------------------------------------------------------------------------

import sys
from distutils.core import setup

v = sys.version_info
if v[:2] < (2,7) or (v[0] >= 3 and v[:2] < (3,3)):
    error = "ERROR: %s requires Python version 2.7 or 3.3 or above." % name
    print(error, file=sys.stderr)
    sys.exit(1)

PY3 = (sys.version_info[0] >= 3)

#-----------------------------------------------------------------------------
# get on with it
#-----------------------------------------------------------------------------


if 'develop' in sys.argv or any(a.startswith('bdist') for a in sys.argv):
    import setuptools

setup_args = dict(
    name                 = 'dask-labextension',
    packages             = ['dask_labextension'],
    version              = '0.0.2',
    author               = 'Luke Canavan and Brian Granger',
    author_email         = 'canavandl@gmail.com',
    keywords             = ['jupyterlab', 'jupyterlab extension', 'dask'],
    install_requires     = ['jupyterlab>=0.7.0'],
    include_package_data = True
)

if __name__ == '__main__':
    setup(**setup_args)
