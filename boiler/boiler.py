# -*- coding: utf-8 -*-

"""
<Description>
"""


class Boiler:
    def __init__(self):
        pass

    @staticmethod
    def boil(value: int) -> int:
        print("Boiling: {}".format(value))
        return value * 2

    def do_stuff(self):
        return None
