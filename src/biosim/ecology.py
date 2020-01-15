# -*- coding: utf-8 -*-

__author__ = "Elinor Skårås og Lisa Hoff"
__email__ = "elinor2511@gmail.com, lisast@nmbu.no"

from src.biosim.animals import Animals as Ani


class Ecology:
    def __init__(self, herbivores, carnivores, age, weight, loc):  # help input
        self.num_herbivores = len(herbivores)
        self.num_carnivores = len(carnivores)
        self.fodder_available = 0
        self.herbivores = herbivores
        self.carnivores = carnivores

    def fodder_available(self):
        herbivores_sorted = sorted(self.herbivores, key=lambda x: x.fitness,
                                   reverse=True)
        for herbivore in herbivores_sorted:
            self.fodder_available -= Ani.feeding_herbivores(
                self.fodder_available)

    def carnivores_prey(self):
        herbivores_sorted = sorted(self.herbivores, key=lambda x: x.fitness,
                                   reverse=False)
        carnivores_sorted = sorted(self.carnivores, key=lambda x: x.fitness,
                                   reverse=True)

        failed_prey = herbivores_sorted

        for carnivore in carnivores_sorted:
            killed = Ani.carnivores_prey(failed_prey)
            if len(killed) > 0:
                for killed_prey in killed:
                    failed_prey.remove(killed_prey)

            self.herbivores = failed_prey

    def procreation_herbivores(self):
        offsprings_herbivores = []

        for herbivore in self.herbivores:
            num_herbivores = len(self.herbivores)
            offspring = Ani.birth(num_herbivores)
            if offspring is not False:
                offsprings_herbivores.append(offspring)

        self.herbivores.extend(offsprings_herbivores)

    def procreation_carnivores(self):
        offsprings_carnivores = []

        for carnivore in self.carnivores:
            num_carnivores = len(self.carnivores)
            offspring = Ani.birth(num_carnivores)
            if offspring is not False:
                offsprings_carnivores.append(offspring)
        self.herbivores.extend(offsprings_carnivores)

    def migration(self):
        pass

    def aging(self):
        pass

    def loss_of_weight(self):
        pass

    def death(self):
        pass


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
            if param == 'possible_to_enter' and value is not (False or True):
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
            if param == 'possible_to_enter' and value is not (False or True):
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
            if param == 'possible_to_enter' and value is not (False or True):
                raise TypeError(value, ': must be True or False')
            else:
                cls.mountain_params[param] = value
