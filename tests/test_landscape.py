# -*- coding: utf-8 -*-

__author__ = "Elinor Skårås og Lisa Hoff"
__email__ = "elinor2511@gmail.com, lisast@nmbu.no"

from src.biosim.landscape import Landscape as Lan

import unittest
import pytest
import textwrap

class TestLandscape(unittest.TestCase):
    def test_div_landscape(self):
        pass

    def test_ocean_around_island(self):
        geostring1 = """\
                        OOOO
                        MMJO
                        OJMO
                        OOOO"""
        geostring2 = """\
                        OOOM
                        OMJO
                        OJMO
                        OOOO"""
        geostring3 = """\
                        OOMO
                        OMJO
                        OJMO
                        OOOO"""
        geostring4 = """\
                        OOOO
                        OMJO
                        OJMO
                        OMOO"""

        geostring5 = """\
                        OOOO
                        OMJO
                        OJMO
                        OMMO"""


        with pytest.raises(ValueError):
            landscape, geostring_list = Lan.create_landscape(self, geostring1)
            landscape, geostring_list = Lan.create_landscape(self, geostring2)
            landscape, geostring_list = Lan.create_landscape(self, geostring3)
            landscape, geostring_list = Lan.create_landscape(self, geostring4)
            landscape, geostring_list = Lan.create_landscape(self, geostring5)




