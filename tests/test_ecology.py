# -*- coding: utf-8 -*-

__author__ = "Elinor Skårås og Lisa Hoff"
__email__ = "elinor2511@gmail.com, lisast@nmbu.no"


from src.biosim.ecology import Ecology as Eco
from src.biosim.ecology import Ocean as Oce
from src.biosim.ecology import Jungle as Jun
from src.biosim.ecology import Savannah as Sav
from src.biosim.ecology import Desert as Des
from src.biosim.ecology import Mountain as Mon
import pytest
# import random
import unittest


class TestOcean:
    def test_errors_set_parameters_ocean(self):
        with pytest.raises(KeyError):
            Oce.set_parameters({'test': 2})
        with pytest.raises(ValueError):
            Oce.set_parameters({'f_max': -2})
        with pytest.raises(TypeError):
            Oce.set_parameters({'Possible_to_enter': 0})




class TestJungle:
    pass


class TestSavannah:
    pass


class TestDesert:
    pass


class TestMountain:
    pass