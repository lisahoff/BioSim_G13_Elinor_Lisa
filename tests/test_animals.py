# -*- coding: utf-8 -*-

__author__ = "Elinor Skårås og Lisa Hoff"
__email__ = "elinor2511@gmail.com, lisast@nmbu.no"


from src.biosim.animals import Animals as Ani
from src.biosim.animals import Carnivores as Carn
from src.biosim.animals import Herbivores as Herb
import pytest
# import random
import unittest


class TestAnimals(unittest.TestCase):  #
    def test_new_birth_weight(self, random_call):
        pass

    def test_new_born_age(self):
        pass

    def test_new_age(self):
        age = 2
        self.age = age
        Ani.aging(self)
        self.assertEqual(self.age, age+1)

    def test_feeding_herbivores(self):
        fodder_available = 20
        self.F = 10
        fodder_eaten = Ani.feeding_herbivores(self, fodder_available)
        self.assertEqual(fodder_eaten, 10)

        fodder_available = 5
        self.F = 10
        fodder_eaten = Ani.feeding_herbivores(self, fodder_available)
        self.assertEqual(fodder_eaten, 5)

    def test_feeding_carnivores(self):
        pass

    def test_increased_weight(self):
        self.weight = 10
        fodder_eaten = 1
        self.beta = 2
        Ani.weight_increase(self, fodder_eaten)
        self.assertEqual(self.weight, 10 + 2*1)

    def test_decreased_weight(self):
        self.weight = 10
        self.eta = 0.5
        Ani.weight_decrease(self)
        self.assertEqual(self.weight, 10 - 10 * 0.5)

    def test_calculate_fitness(self):
        self.phi_age = 0.2
        self.age = 8
        self.a_half = 40
        self.phi_weight = 0.1
        self.w_half = 10
        self.w_birth = 8

        self.weight = 7
        self.fitness = Ani.calculate_fitness(self)
        wanted_fitness = 0
        self.assertEqual(self.fitness, wanted_fitness)

        self.weight = 10
        self.fitness = Ani.calculate_fitness(self)
        self.assertAlmostEqual(float(self.fitness), 0.4991, 3)

    def test_migration(self):
        pass

    def test_birth(self):
        pass

    def test_death(self):
        pass


class TestHerbivore(unittest.TestCase):
    def test_errors_new_parameters_herb(self):
        with pytest.raises(KeyError):
            Herb.set_parameters({'test': 2})
        with pytest.raises(ValueError):
            Herb.set_parameters({'omega': -2})
        with pytest.raises(ValueError):
            Herb.set_parameters({'DeltaPhiMax': 0})
        with pytest.raises(ValueError):
            Herb.set_parameters({'eta': 1.1})


class TestCarnivore(unittest.TestCase):
    def test_errors_new_parameters_carn(self):
        with pytest.raises(KeyError):
            Carn.set_parameters({'test': 2})
        with pytest.raises(ValueError):
            Carn.set_parameters({'omega': -2})
        with pytest.raises(ValueError):
            Carn.set_parameters({'DeltaPhiMax': 0})
        with pytest.raises(ValueError):
            Carn.set_parameters({'eta': 1.1})
