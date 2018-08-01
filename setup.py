# -*- coding: utf-8 -*-

"""
<Description>
"""

import setuptools

AUTHOR = "Jakrin Juangbhanich"
EMAIL = "krinj@genvis.co"
PACKAGE_NAME = "boiler"
REPO = "https://github.com/Infrarift/py-cicd-boiler"

with open("support/version", "r") as f:
    VERSION = f.readline()

setuptools.setup(
    author=AUTHOR,
    author_email=EMAIL,
    name=PACKAGE_NAME,
    version=VERSION,
    url=REPO,
    packages=setuptools.find_packages(),
    test_suite='nose.collector',
    tests_require=['nose'],
    # add the dependencies of the package here
    install_requires=[
        # 'numpy==1.14.5',
    ],
)

with open("upload_to_nexus.sh", 'w') as f:
    f.write('#!/usr/bin/env bash\n')
    f.write('pip install twine\n')
    f.write('twine upload -r pypi-local --repository-url https://nexus.genvis.co/repository/pypi-local/ -u dev -p '
            'usainbolt2018 dist/{}-{}.tar.gz\n'.format(
        PACKAGE_NAME,
        VERSION
    )
    )
