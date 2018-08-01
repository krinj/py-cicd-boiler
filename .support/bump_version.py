#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Bump the micro-version number of the package.
"""
import os

if __name__ == "__main__":

    with open(".support/version", "r") as f:
        current_version = f.readline()
        versions = current_version.split(".")
        versions[-1] = str(int(versions[-1]) + 1)
        new_version = ".".join(versions)

    with open(".support/version", "w") as f:
        f.write(new_version)

    print("Bumping Version Number: {} -> {}".format(current_version, new_version))
    os.system("git add .support/version")
