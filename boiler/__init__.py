# -*- coding: utf-8 -*-

"""
<Description>
"""

__author__ = "Jakrin Juangbhanich"
__copyright__ = "Copyright 2018, GenVis Pty Ltd."
__email__ = "krinj@genvis.co"

# Make these accessible at the root namespace.
from .boiler import Boiler
from .heater import Heater

with open("version", "r") as f:
    __version__ = f.readline()

