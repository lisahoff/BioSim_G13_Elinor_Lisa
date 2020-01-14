# -*- coding: utf-8 -*-

__author__ = "Elinor Skårås og Lisa Hoff"
__email__ = "elinor2511@gmail.com, lisast@nmbu.no"


class Ocean(Ecology):
    ocean_params = {'f_max': 0,
                    'possible_to_enter': False}

    def __init__(self, herbivores=None, carnivores=None, age=0, weight=0,
                 loc=None):
        super().__init__(herbivores, carnivores, age, weight, loc)  #
        self.fodder = self.ocean_params['f_max']

    @classmethod
    def set_parameters(cls, new_params):
        for param, value in new_params.items():
            if param not in cls.ocean_params:
                raise KeyError(param, ': must be a ocean parameter.')
            if value < 0:
                raise ValueError(value, ': must be positive.')
            if param == 'possible_to_enter' and not (False or True):
                raise TypeError(value, ': must be True or False')
            else:
                cls.ocean_params[param] = value


class Jungle(Ecology):
    jungle_params = {'f_max': 800,
                     'possible_to_enter': True}

    def __init__(self, herbivores=None, carnivores=None, age=0, weight=0,
                 loc=None):
        super().__init__(herbivores, carnivores, age, weight, loc)  #
        self.fodder = self.jungle_params['f_max']

    def grow_fodder(self):
        self.fodder = self.jungle_params['f_max']

    @classmethod
    def set_parameters(cls, new_params):
        for param, value in new_params.items():
            if param not in cls.jungle_params:
                raise KeyError(param, ': must be a jungle parameter.')
            if value < 0:
                raise ValueError(value, ': must be positive.')
            if param == 'possible_to_enter' and not (False or True):
                raise TypeError(value, ': must be True or False')
            else:
                cls.jungle_params[param] = value


class Savannah(Ecology):
    savannah_params = {'f_max': 300,
                       'alpha': 0.3,
                       'possible_to_enter': True}

    def __init__(self, herbivores=None, carnivores=None, age=0, weight=0,
                 loc=None):
        super().__init__(herbivores, carnivores, age, weight, loc)  #
        self.fodder = self.savannah_params['f_max']

    def grow_fodder(self):
        self.fodder = self.fodder + self.savannah_params['alpha'] * (
                    self.savannah_params['f_max'] - self.fodder)

    @classmethod
    def set_parameters(cls, new_params):
        for param, value in new_params.items():
            if param not in cls.savannah_params:
                raise KeyError(param, ': must be a savannah parameter.')
            if value < 0:
                raise ValueError(value, ': must be positive.')
            if param == 'possible_to_enter' and not (False or True):
                raise TypeError(value, ': must be True or False')
            else:
                cls.savannah_params[param] = value


class Desert(Ecology):
    desert_params = {'f_max': 0,
                     'possible_to_enter': False}  # Kun carnivores

    def __init__(self, herbivores=None, carnivores=None, age=0, weight=0,
                 loc=None):
        super().__init__(herbivores, carnivores, age, weight, loc)  #
        self.fodder = self.desert_params['f_max']

    @classmethod
    def set_parameters(cls, new_params):
        for param, value in new_params.items():
            if param not in cls.desert_params:
                raise KeyError(param, ': must be a desert parameter.')
            if value < 0:
                raise ValueError(value, ': must be positive.')
            if param == 'possible_to_enter' and not (False or True):
                raise TypeError(value, ': must be True or False')
            else:
                cls.desert_params[param] = value


class Mountain(Ecology):
    mountain_params = {'f_max': 0,
                       'possible_to_enter': False}

    def __init__(self, herbivores=None, carnivores=None, age=0, weight=0,
                 loc=None):
        super().__init__(herbivores, carnivores, age, weight, loc)  #
        self.fodder = self.mountain_params['f_max']

    @classmethod
    def set_parameters(cls, new_params):
        for param, value in new_params.items():
            if param not in cls.mountain_params:
                raise KeyError(param, ': must be a mountain parameter.')
            if value < 0:
                raise ValueError(value, ': must be positive.')
            if param == 'possible_to_enter' and not (False or True):
                raise TypeError(value, ': must be True or False')
            else:
                cls.mountain_params[param] = value
