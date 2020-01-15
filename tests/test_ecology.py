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


class Ecology(unittest.TestCase):
    def test_fodder_available_update(self):
        pass

    def test_carnivores_prey(self):
        pass

    def test_procreation_herbivores(self):
        pass

    def test_procreation_carnivores(self):
        pass

    def test_migration(self):
        pass

    def test_aging(self):
        pass

    def test_loss_of_weight(self):
        pass

    def test_death(self):
        pass


class TestOcean(unittest.TestCase):
    def test_errors_set_parameters_ocean(self):
        with pytest.raises(KeyError):
            Oce.set_parameters({'test': 2})
        with pytest.raises(ValueError):
            Oce.set_parameters({'f_max': -2})
        with pytest.raises(TypeError):
            Oce.set_parameters({'possible_to_enter': 0})


class TestJungle(unittest.TestCase):
    def test_errors_set_parameters_jungle(self):
        with pytest.raises(KeyError):
            Jun.set_parameters({'test': 2})
        with pytest.raises(ValueError):
            Jun.set_parameters({'f_max': -2})
        with pytest.raises(TypeError):
            Jun.set_parameters({'possible_to_enter': 0})


class TestSavannah(unittest.TestCase):
    def test_errors_set_parameters_savannah(self):
        with pytest.raises(KeyError):
            Sav.set_parameters({'test': 2})
        with pytest.raises(ValueError):
            Sav.set_parameters({'f_max': -2})
        with pytest.raises(TypeError):
            Sav.set_parameters({'possible_to_enter': 0})


class TestDesert(unittest.TestCase):
    def test_errors_set_parameters_desert(self):
        with pytest.raises(KeyError):
            Des.set_parameters({'test': 2})
        with pytest.raises(ValueError):
            Des.set_parameters({'f_max': -2})
        with pytest.raises(TypeError):
            Des.set_parameters({'possible_to_enter': 0})


class TestMountain(unittest.TestCase):
    def test_errors_set_parameters_mountain(self):
        with pytest.raises(KeyError):
            Mon.set_parameters({'test': 2})
        with pytest.raises(ValueError):
            Mon.set_parameters({'f_max': -2})
        with pytest.raises(TypeError):
            Mon.set_parameters({'possible_to_enter': 0})