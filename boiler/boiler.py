# -*- coding: utf-8 -*-

"""
<Description>
"""

__author__ = "Jakrin Juangbhanich"
__copyright__ = "Copyright 2018, GenVis Pty Ltd."
__email__ = "krinj@genvis.co"


class Boiler:
    def __init__(self):
        pass

    @staticmethod
    def boil(value: int) -> int:
        print("Boiling: {}".format(value))
        return value * 2
