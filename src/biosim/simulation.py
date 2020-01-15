# -*- coding: utf-8 -*-

"""
"""

__author__ = "Elinor Skårås og Lisa Hoff Strøm"
__email__ = "elinor2511@gmail.com, lisast@nmbu.no"

import random

class BioSim:
    def __init__(
        self,
        island_map,
        ini_pop,
        seed,
        ymax_animals=None,
        cmax_animals=None,
        img_base=None,
        img_fmt="png",
    ):
        """
        :param island_map: Multi-line string specifying island geography
        :param ini_pop: List of dictionaries specifying initial population
        :param seed: Integer used as random number seed
        :param ymax_animals: Number specifying y-axis limit for graph showing animal numbers
        :param cmax_animals: Dict specifying color-code limits for animal densities
        :param img_base: String with beginning of file name for figures, including path
        :param img_fmt: String with file type for figures, e.g. 'png'

        If ymax_animals is None, the y-axis limit should be adjusted automatically.

        If cmax_animals is None, sensible, fixed default values should be used.
        cmax_animals is a dict mapping species names to numbers, e.g.,
           {'Herbivore': 50, 'Carnivore': 20}

        If img_base is None, no figures are written to file.
        Filenames are formed as

            '{}_{:05d}.{}'.format(img_base, img_no, img_fmt)

        where img_no are consecutive image numbers starting from 0.
        img_base should contain a path and beginning of a file name.
        """
        self.island_map = island_map
        self.landscape = []
        self.island_map_split = island_map.split()
        self.column = len(island_map.split()[0])
        self.row = len(island_map.split())
        self.island_map_list = []
        self.landscape_types = ['O', 'J', 'S', 'D', 'M']

        self.ini_pop = ini_pop
        self.herbivores = []
        self.carnivores = []

        self.seed = random.seed()

    def create_landscape(self):
        for row_island_map in range(0, self.row):
            for element in self.island_map_split[row_island_map]:
                self.island_map_list.append(element)

        if len(self.island_map_list) % self.row != 0 or \
            len(self.island_map_list) % self.column != 0:
            raise ValueError('the island is not a foursquare')

        island_map_str = ''.join(self.island_map_list)
        n = 0
        for i in range(self.row):
            for j in range(self.column):
                coord = (i, j)
                self.landscape.append({"loc": coord, "lan": island_map_str[n]})
                if island_map_str[n] not in self.landscape_types:
                    raise ValueError(island_map_str[n], 'is not a landscape type.')
                n += 1

        for north_coord in self.island_map_list[:self.column]:
            if north_coord != 'O':
                raise ValueError('the island is not surrounded by ocean.')
        for south_coord in self.island_map_list[self.column * (self.row - 1):]:
            if south_coord != 'O':
                raise ValueError('the island is not surrounded by ocean.')
        for west_coord in self.island_map_list[0::self.column]:
            if west_coord != 'O':
                raise ValueError('the island is not surrounded by ocean.')
        for east_coord in self.island_map_list[(self.column - 1)::self.column]:
            if east_coord != 'O':
                raise ValueError('the island is not surrounded by ocean.')

        return self.landscape, self.island_map_list

    #@classmethod
    #def island_surrounded_by_ocean:

    def populate_island(self):
        for coord in range(len(self.ini_pop)):
            self.loc = self.ini_pop[coord]['loc']  ###
            population = self.ini_pop[coord]['pop']
            for animal in range(len(population)):
                self.species = population[animal]['species']
                self.age = population[animal]['age']
                self.weight = population[animal]['weight']
                if self.species == 'Herbivore':
                    self.herbivores.append(
                        {'age': self.age, 'weight': self.weight,
                         'loc': self.loc})
                if self.species == 'Carnivore':
                    self.carnivores.append(
                        {'age': self.age, 'weight': self.weight,
                         'loc': self.loc})
                # else:
                    # raise ValueError('The list of animals has wrong species')
        return self.herbivores, self.carnivores

    def set_animal_parameters(self, species, params):
        """
        Set parameters for animal species.

        :param species: String, name of animal species
        :param params: Dict with valid parameter specification for species
        """
        pass

    def set_landscape_parameters(self, landscape, params):
        """
        Set parameters for landscape type.

        :param landscape: String, code letter for landscape
        :param params: Dict with valid parameter specification for landscape
        """
        pass

    def simulate(self, num_years, vis_years=1, img_years=None):
        """
        Run simulation while visualizing the result.

        :param num_years: number of years to simulate
        :param vis_years: years between visualization updates
        :param img_years: years between visualizations saved to files (default: vis_years)

        Image files will be numbered consecutively.
        """
        pass

    def add_population(self, population):
        """
        Add a population the island

        :param population: List of dictionaries specifying population
        """
        pass

    @property
    def year(self):
        """Last year simulated."""
        pass

    @property
    def num_animals(self):
        """Total number of animals on island."""
        pass

    @property
    def num_animals_per_species(self):
        """Number of animals per species in island, as dictionary."""
        pass

    @property
    def animal_distribution(self):
        """Pandas DataFrame with animal count per species for each cell on island."""
        pass

    def make_movie(self):
        """Create MPEG4 movie from visualization images saved."""
        pass


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

    Landscape = BioSim(geostring, poplist,seed =0, ymax_animals=None,
        cmax_animals=None,
        img_base=None,
        img_fmt="png")
    landscape, geostring_list = Landscape.create_landscape()
    print(landscape)

    herb, carn = Landscape.populate_island()
    print(herb)
    print(carn)

