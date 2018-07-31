# -*- coding: utf-8 -*-

"""
<Description>
"""

from unittest import TestCase
from boiler import Boiler

__author__ = "Jakrin Juangbhanich"
__copyright__ = "Copyright 2018, GenVis Pty Ltd."
__email__ = "krinj@genvis.co"


class TestBoiler(TestCase):
    def test_boil(self):
        boiler: Boiler = Boiler
        boiler.boil(10)
