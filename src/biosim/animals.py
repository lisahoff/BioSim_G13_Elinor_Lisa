# -*- coding: utf-8 -*-

__author__ = "Elinor Skårås og Lisa Hoff"
__email__ = "elinor2511@gmail.com, lisast@nmbu.no"


class Herbivores(Animals):
    herbivore_params = {'w_birth': 8,
                        'sigma_birth': 1.5,
                        'beta': 0.9,
                        'eta': 0.05,
                        'a_half': 40,
                        'phi_age': 0.2,
                        'w_half': 10,
                        'phi_weight': 0.1,
                        'mu': 0.25,
                        'lamdba': 1,
                        'gamma': 0.2,
                        'zeta': 3.5,
                        'xi': 1.2,
                        'omega': 0.4,
                        'F': 10,
                        'DeltaPhiMax': None}

    def __init__(self, age=0, weight=None, loc=None):
        super().__init__(age, weight, loc)  #

    @classmethod
    def set_parameters(cls, new_params):
        for param, value in new_params.items():
            if param not in cls.herbivore_params:
                raise KeyError(param, ': must be a herbivore parameter.')
            if value < 0:
                raise ValueError(value, ': must be positive.')
            if param == 'DeltaPhiMax' and value <= 0:
                raise ValueError(value, ': must be strictly positive')
            if param == 'eta' and value > 1:
                raise ValueError(value, ': must be lower or equal to 1.')
            else:
                cls.herbivore_params[param] = value


class Carnivores(Animals):

    carnivore_params =      {'w_birth': 6,
                             'sigma_birth': 1,
                             'beta': 0.75,
                             'eta': 0.125,
                             'a_half': 60,
                             'phi_age': 0.4,
                             'w_half': 4,
                             'phi_weight': 0.4,
                             'mu': 0.4,
                             'lamdba': 1,
                             'gamma': 0.8,
                             'zeta': 3.5,
                             'xi': 1.1,
                             'omega': 0.9,
                             'F': 50,
                             'DeltaPhiMax': 10}

    def __init__(self, age=0, weight=None, loc = None):
        super().__init__(age, weight, loc) ###

    @classmethod
    def set_parameters(cls, new_params):
        for param, value in new_params.items():
            if param not in cls.carnivore_params:
                raise KeyError(param, ': must be a carnivore parameter.')
            if value < 0:
                raise ValueError(value, ': must be positive.')
            if param == 'DeltaPhiMax' and value <= 0:
                raise ValueError(value, ': must be strictly positive')
            if param == 'eta' and value > 1:
                raise ValueError(value, ': must be lower or equal to 1.')
            else:
                cls.carnivore_params[param] = value
