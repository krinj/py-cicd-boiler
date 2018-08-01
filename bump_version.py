#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Bump the micro-version number of the package.
"""


if __name__ == "__main__":

    with open("VERSION", "r") as f:
        current_version = f.readline()
        versions = current_version.split(".")
        versions[-1] = str(int(versions[-1]) + 1)
        new_version = ".".join(versions)

    with open("VERSION", "w") as f:
        f.write(new_version)

    print("Bumping Version Number: {} -> {}".format(current_version, new_version))
