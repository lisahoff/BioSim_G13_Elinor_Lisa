# -*- coding: utf-8 -*-

__author__ = "Elinor Skårås og Lisa Hoff"
__email__ = "elinor2511@gmail.com, lisast@nmbu.no"

import random
import math


class Animals():
    '''
    Class for all animals on island
    '''
    def __init___(self, age=0, weight=None, loc=None):
        ''' creates animal with age 0

        Parameters
        ----------
        age: int - starting age for animal
        weight: float - starting weight for animal
        loc: type of location

        Returns
        -------

        '''
        self.age = age
        if weight:
            self.weight = weight
        else:
            self.weight = random.gauss(self.w_birth, self.sigma_birth)
        self.loc = loc
        self.fitness = 0

    def aging(self):
        '''

        Returns the amount of years the animal ages
        -------

        '''
        self.age += 1
        # self.calculate_fitness()

    def feeding_herbivores(self, fodder_available):
        '''

        Parameters
        ----------
        fodder_available is the fodder available in the cell before the
        herbivore starts to eat.

        Returns the amount of fodder eaten by the herbivore.
        -------

        '''
        if fodder_available > self.F:
            fodder_eaten = self.F
            fodder_available -= self.F
        else:
            fodder_eaten = fodder_available
        return fodder_eaten

    def feeding_carnivores(self, failed_prey):
        '''

        Parameters
        ----------
        failed_prey are the number of herbivores that survives the attack
        from carnivores when the carnivore faills to kill

        Returns the list of herbivores eaten
        -------

        '''
        killed = []
        killed_herbivores = 0

        if self.killed_herbivores < self.F and failed_prey > 0:
            carnivore_fitness = self.calculate_fitness()
            for prey in failed_prey:
                herbivore_fitness = prey.calulate_fitness()
                if carnivore_fitness <= herbivore_fitness:
                    probability = 0
                elif (
                        carnivore_fitness - herbivore_fitness) \
                        < self.DeltaPhiMax:
                    probability = (carnivore_fitness - herbivore_fitness) \
                                  / self.DeltaPhiMax
                else:
                    probability = 1
                if random.uniform(0, 1) < probability:
                    killed.append(prey)
                    killed_herbivores += prey.weight
                    self.weight += self.beta * prey.weight

        return killed

    def weight_increase(self, fodder_eaten):
        '''

        Parameters
        ----------
        fodder_eaten is the fodder which is eaten by the animal

        Increases the animal weight due to x amount of fodder eaten * the
        parameter 'beta'
        -------

        '''
        self.weight += fodder_eaten * self.beta
        # self.calculate_fitness()

    def weight_decrease(self):
        '''

        Decreases the animal weight annually based on the parameter 'eta'
        -------

        '''
        self.weight -= self.weight * self.eta
        # self.calculate_fitness()

    def calculate_fitness(self):
        ''' The calculated fitness level of animal which is based
        on age and weight of the animal.

        Returns a float of the calculated fitness level.
        -------

        '''
        if self.weight <= self.w_birth:
            self.fitness = 0
        else:
            self.fitness = (1 / (1 + math.exp(
                self.phi_age * (self.age - self.a_half)))) * \
                           (1 / (1 + math.exp(
                               self.phi_weight * (self.weight - self.w_half))))
        return self.fitness

<<<<<<< Updated upstream
    def will_migrate(self):
=======
    def migration(self):
        '''

        Returns boolean if the animal migrate, depending on their
        own fitness and the availability of fodder in neighboring cells
        -------

        '''
>>>>>>> Stashed changes
        probability = self.mu * self.fitness
        if random.uniform(0, 1) < probability:
            return True
        else:
            return False

    def birth(self, num_animals):
        '''

        Parameters
        ----------
        num_animals: is the number of animals in the given cell

        Returns offspring if the animal gives birth during a year and updates
        the mother animals weight depending on the birth weight. If no birth
        is given the mother weight stays the same.

        -------

        '''
        if self.weight < self.zeta * (self.w_birth + self.sigma_birth):
            probability = 0
        else:
            probability = min(1, self.gamma * self.fitness * num_animals - 1)

        if random.uniform(0, 1) < probability:
            offspring = self.__class__(loc=self.loc)
            if self.weight - self.w_birth * self.xi > 0:
                self.weight = - self.w_birth * self.xi
                self.calculate_fitness()
                return offspring
        else:
            return False

    def death(self):
        '''

        Returns the probability of an animal dying during a year
        -------

        '''
        probability = self.omega * (1 - self.fitness)
        if random.uniform(0, 1) < probability:
            return True
        else:
            return False


class Herbivores(Animals):
        '''
        Class parameters represented in a dictionary.
        '''

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
        super().__init__(age, weight, loc) #


    @classmethod
    def set_parameters(cls, new_params):
        '''

        Parameters
        ----------
        new_params

        Returns
        -------

        '''
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
        '''
        Class parameters represented in a dictionary.

        '''
    carnivore_params = {'w_birth': 6,
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

    def __init__(self, age=0, weight=None, loc=None):
        super().__init__(age, weight, loc)  #

    @classmethod
    def set_parameters(cls, new_params):
        '''

        Parameters
        ----------
        new_params

        Returns
        -------

        '''
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
