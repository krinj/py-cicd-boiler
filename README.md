# Python CI-CD Boiler Plate Project
[![Build Status](https://travis-ci.org/Infrarift/py-cicd-boiler.svg?branch=master)](https://travis-ci.org/Infrarift/py-cicd-boiler) [![codecov](https://codecov.io/gh/Infrarift/py-cicd-boiler/branch/master/graph/badge.svg)](https://codecov.io/gh/Infrarift/py-cicd-boiler) ![Version](https://img.shields.io/badge/version-0.3.32-333333.svg)

This is a boiler plate project for Python packages. It includes a minimal example package, and some support scripts for making developing and updating it easier.

## Features

- [Travis CI Integration](https://travis-ci.com).
- Unit Tests.
- [Code Coverage](https://codecov.io).
- Script to automatically upload package to a nexus PyPI repository on push.
- Automatic Version Bumping (as a git hook).
- Automatic README badges.

## Getting Started

#### Auto Version Management

First, run this script from the root directory of the project to set up the local git hooks.

```bash
bash .support/setup.sh
```

This will set up the automatic version bumping. It will update the micro version string in `version` file, which is used by `setup.py` to generate the package version, and also injected into the `__init__.py` file of the package so that when imported, the user can use `<package>.__version__` . This will be done as a git hook on every commit. Major and minor versions must be updated manually.

#### 3rd Party Services

To use this, you will need to hook up this repository with a [Travis account](travis-ci.org), a [CodeCov](https://codecov.io) account, and some kind of online repository, like Nexus.

#### Setup Config

Modify the fields at the top of `setup.py`:

```python
AUTHOR = "Jakrin Juangbhanich"
EMAIL = "krinj@genvis.co"
PACKAGE_NAME = "boiler"
DESCRIPTION = "A boiler-plate project for packages."
REPO = "https://github.com/Infrarift/py-cicd-boiler"
```

The `PACKAGE_NAME` also specifies the directory which will be exported and bundled (and will be also the name of the package). Everything under that directory will be exported, and everything outside will not.

If you want to export some other packages, or have more custom control, modify this line in the setup script instead:

```python
packages=["foo", "bar"]
```

#### Unit Tests

Unit tests should be named in the format of `test_*.py` and should reside in the `tests` directory. These tests will be run automatically by the Travis service.