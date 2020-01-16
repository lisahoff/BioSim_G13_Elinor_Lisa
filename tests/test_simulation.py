# -*- coding: utf-8 -*-

__author__ = "Elinor Skårås og Lisa Hoff"
__email__ = "elinor2511@gmail.com, lisast@nmbu.no"

from src.biosim.simulation import BioSim as BioSim
# Ikke ferdig
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

        lan1 = Lan(geostring1)
        lan2 = Lan(geostring2)
        lan3 = Lan(geostring2)
        lan4 = Lan(geostring2)
        lan5 = Lan(geostring2)

        with pytest.raises(ValueError):
            landscape, geostring_list = lan1.create_landscape()
            landscape, geostring_list = lan2.create_landscape()
            landscape, geostring_list = lan3.create_landscape()
            landscape, geostring_list = lan4.create_landscape()
            landscape, geostring_list = lan5.create_landscape()

    def test_string_landscape_types(self):
        geostring = """\
                        OOOO
                        OOOO
                        OKKO
                        OOOO"""

        with pytest.raises(ValueError):
            landscape, geostring_list = Lan.create_landscape(self, geostring)

    def test_string_is_foursquare(self):
        geostring = """\
                        OOO
                        OOOO
                        OKKO
                        OOOO"""

        with pytest.raises(ValueError):
            landscape, geostring_list = Lan.create_landscape(self, geostring)


