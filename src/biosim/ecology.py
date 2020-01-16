# -*- coding: utf-8 -*-

__author__ = "Elinor Skårås og Lisa Hoff"
__email__ = "elinor2511@gmail.com, lisast@nmbu.no"

from src.biosim.animals import Animals as Ani
from src.biosim.animals import Herbivores as Herb
from src.biosim.animals import Carnivores as Carn
from src.biosim.simulation import BioSim as Bio


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
        self.herbivores = [(age, weight, loc) for _ in range(num_herbivores)]
        self.carnivores = [(age, weight, loc) for _ in range(num_carnivores)]
        print(self.herbivores)
        print(self.carnivores)
        print('_________')


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
            offspring = Ani.birth(self.num_herbivores)
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
            offspring = Ani.birth(self.num_carnivores)
            if offspring is not False:
                offsprings_carnivores.append(offspring)
        self.herbivores.extend(offsprings_carnivores)

    def migration(self):
        '''

        Returns
        -------

        '''
        pass

    def aging_animals(self):
        '''

        Returns
        -------

        '''
        for herb in self.herbivores:
            Ani.aging()
        for carn in self.carnivores:
            Ani.aging()

    def loss_of_weight_animals(self):
        '''

        Returns
        -------

        '''
        for herb in self.herbivores:
            Ani.weight_decrease()
        for carn in self.carnivores:
            Ani.weight_decrease()

    def dead_animals(self):
        '''

        Returns
        -------

        '''
        living_herbivores = []
        for herb in self.herbivores:
            if Ani.calculate_fitness(self) != 0:
                if Ani.death is True:
                    pass
            else:
                living_herbivores.append(herb)



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

    def __init__(self, num_herbivores=None, num_carnivores=None, age=0, weight=0,
                 loc=None):
        super().__init__(num_herbivores, num_carnivores, age, weight, loc)  #
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

    def __init__(self, num_herbivores=None, num_carnivores=None, age=0, weight=0,
                 loc=None):
        super().__init__(num_herbivores, num_carnivores, age, weight, loc)  #
        self.fodder = self.jungle_params['f_max']

    def grow_fodder(self):
        '''

        Returns
        -------

        '''
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

    def __init__(self, num_herbivores=None, num_carnivores=None, age=0, weight=0,
                 loc=None):
        super().__init__(num_herbivores, num_carnivores, age, weight, loc)  #
        self.fodder = self.savannah_params['f_max']

    def grow_fodder(self):
        '''

        Returns
        -------

        '''
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

    def __init__(self, num_herbivores=None, num_carnivores=None, age=0, weight=0,
                 loc=None):
        super().__init__(num_herbivores, num_carnivores, age, weight, loc)  #
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

    def __init__(self, num_herbivores=None, num_carnivores=None, age=0, weight=0,
                 loc=None):
        super().__init__(num_herbivores, num_carnivores, age, weight, loc)  #
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


if __name__ == "__main__":

    poplist = [{'loc': (3,4),
      'pop': [{'species': 'Herbivore', 'age': 10, 'weight': 15},
              {'species': 'Herbivore', 'age': 5, 'weight': 40},
              {'species': 'Herbivore', 'age': 15, 'weight': 25}]},
     {'loc': (4,4),
      'pop': [{'species': 'Herbivore', 'age': 2, 'weight': 60},
              {'species': 'Herbivore', 'age': 9, 'weight': 30},
              {'species': 'Herbivore', 'age': 16, 'weight': 14}]},
     {'loc': (4,4),
      'pop': [{'species': 'Carnivore', 'age': 3, 'weight': 35},
              {'species': 'Carnivore', 'age': 5, 'weight': 20},
              {'species': 'Carnivore', 'age': 8, 'weight': 5}]}]


    geogr = """\
               OOOOOOOOOOOOOOOOOOOOO
               OOOOOOOOSMMMMJJJJJJJO
               OSSSSSJJJJMMJJJJJJJOO
               OSSSSSSSSSMMJJJJJJOOO
               OSSSSSJJJJJJJJJJJJOOO
               OSSSSSJJJDDJJJSJJJOOO
               OSSJJJJJDDDJJJSSSSOOO
               OOSSSSJJJDDJJJSOOOOOO
               OSSSJJJJJDDJJJJJJJOOO
               OSSSSJJJJDDJJJJOOOOOO
               OOSSSSJJJJJJJJOOOOOOO
               OOOSSSSJJJJJJJOOOOOOO
               OOOOOOOOOOOOOOOOOOOOO"""

    import textwrap

    geostring = textwrap.dedent(geogr)

    Landscape = Bio(geostring, poplist,seed =0, ymax_animals=None,
        cmax_animals=None,
        img_base=None,
        img_fmt="png")
    landscape, geostring_list = Landscape.create_landscape()
    print(landscape)

    herb, carn = Landscape.populate_island()
    print(herb)
    print(carn)
    age = []
    weight = []

    for animal in range(len(herb)):
        num_herb = len(herb)
        num_carn = len(carn)
        age.append(herb[animal]['age'])
        weight.append(herb[animal]['weight'])
        loc = herb[animal]['loc']

    Eco = Ecology(num_herb, num_carn, age, weight, loc)
    Eco.aging_animal()
    print(age)
