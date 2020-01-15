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
        geostring = """\
                        OOOO
                        MMJO
                        OJMO
                        OOOO"""
        geostring = textwrap.dedent(geostring)

        lan = Lan(geostring)
        landscape, geostring_list = lan.create_landscape(self.geostring)
        with pytest.raises(ValueError):
            lan.ocean_around_island(geostring_list)


