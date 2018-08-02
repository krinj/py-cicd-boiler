# -*- coding: utf-8 -*-

"""
<Description>
"""

import setuptools

AUTHOR = "Jakrin Juangbhanich"
EMAIL = "krinj@genvis.co"
PACKAGE_NAME = "boiler"
REPO = "https://github.com/Infrarift/py-cicd-boiler"


with open("version", "r") as f:
    VERSION = f.readline()


def find_packages_under(path):
    all_packages = setuptools.find_packages()
    packages = []
    for package in all_packages:
        package_split = package.split(".")
        if package_split[0] == path:
            packages.append(package)
    return packages


setuptools.setup(
    author=AUTHOR,
    author_email=EMAIL,
    name=PACKAGE_NAME,
    version=VERSION,
    url=REPO,
    packages=find_packages_under(PACKAGE_NAME),
    install_requires=[],
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
