# -*- coding: utf-8 -*-

__author__ = "Elinor Skårås og Lisa Hoff"
__email__ = "elinor2511@gmail.com, lisast@nmbu.no"

from src.biosim.animals import Animals as Ani


class Ecology:
    '''
       Class for the ecology on island, where carnivores prey, herbivores eat
       fodder, animals give birth, migrate to other cells, they age,
       lose weight and die.
    '''
    def __init__(self, herbivores, carnivores, age, weight, loc):  # help input
        '''
        Parameters
        ----------
        herbivores:
        carnivores:
        age:
        weight:
        loc:

        Returns
        -------

        '''
        self.num_herbivores = len(herbivores)
        self.num_carnivores = len(carnivores)
        self.fodder_available = 0
        self.herbivores = herbivores
        self.carnivores = carnivores

    def fodder_available(self):
        '''

        Returns the amount of fodder available in the cell at the start of
        the simulation
        -------

        '''
        herbivores_sorted = sorted(self.herbivores, key=lambda x: x.fitness,
                                   reverse=True)
        for herbivore in herbivores_sorted:
            self.fodder_available -= Ani.feeding_herbivores(
                self.fodder_available)

    def carnivores_prey(self):
        '''

        Returns
        -------

        '''
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
        '''

        Returns
        -------

        '''
        offsprings_herbivores = []

        for herbivore in self.herbivores:
            num_herbivores = len(self.herbivores)
            offspring = Ani.birth(num_herbivores)
            if offspring is not False:
                offsprings_herbivores.append(offspring)

        self.herbivores.extend(offsprings_herbivores)

    def procreation_carnivores(self):
        '''

        Returns
        -------

        '''
        offsprings_carnivores = []

        for carnivore in self.carnivores:
            num_carnivores = len(self.carnivores)
            offspring = Ani.birth(num_carnivores)
            if offspring is not False:
                offsprings_carnivores.append(offspring)
        self.herbivores.extend(offsprings_carnivores)

    def migration(self):
        '''

        Returns
        -------

        '''
        pass

    def aging(self):
        '''

        Returns
        -------

        '''
        pass

    def loss_of_weight(self):
        '''

        Returns
        -------

        '''
        pass

    def death(self):
        '''

        Returns
        -------

        '''
        pass


class Ocean(Ecology):
    '''
    Sub class for the geography type Ocean

    Parameters
    ----------
    'f_max': 0
    'possible_to_enter': False

    '''
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
    '''
       Sub class for the geography type Jungle

       Parameters
       ----------
       'f_max': 800
       'possible_to_enter': True

       '''
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
    '''
    Sub class for the geography type Savannah

    Parameters
    ----------
    'f_max': 300,
    'alpha': 0.3,
    'possible_to_enter': True

    '''
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
    '''
    Sub Class for the geography type Desert

    Parameters
    ----------
    'f_max': 300,
    'alpha': 0.3,
    'possible_to_enter': True

    '''
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
    '''
    Class for the geography type Mountain

    Parameters
    ----------
    'f_max': 0
    'possible_to_enter': False

    '''
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
