# -*- coding: utf-8 -*-

__author__ = "Elinor Skårås og Lisa Hoff"
__email__ = "elinor2511@gmail.com, lisast@nmbu.no"



class Landscape():
    def __init__ (self, geostring, poplist):
        self.geostring = geostring
        self.landscape = []
        self.geostring_split = geostring.split()
        self.column = len(geostring.split()[0])
        self.row = len(geostring.split())
        self.geostring_list = []
        self.landscape_types = ['O', 'J', 'S', 'D', 'M']

        self.poplist = poplist
        self.herbivores = []
        self.carnivores = []

    def create_landscape(self):
        for row_geostring in range(0, self.row):
            for element in self.geostring_split[row_geostring]:
                self.geostring_list.append(element)

        if len(self.geostring_list) % self.row != 0 or \
            len(self.geostring_list) % self.column != 0:
            raise ValueError('the island is not a foursquare')

        geostring_str = ''.join(self.geostring_list)
        n = 0
        for i in range(self.row):
            for j in range(self.column):
                coord = (i, j)
                self.landscape.append({"loc": coord, "lan": geostring_str[n]})
                if geostring_str[n] not in self.landscape_types:
                    raise ValueError(geostring_str[n], 'is not a landscape type.')
                n += 1

        for north_coord in self.geostring_list[:self.column]:
            if north_coord != 'O':
                raise ValueError('the island is not surrounded by ocean.')
        for south_coord in self.geostring_list[self.column * (self.row - 1):]:
            if south_coord != 'O':
                raise ValueError('the island is not surrounded by ocean.')
        for west_coord in self.geostring_list[0::self.column]:
            if west_coord != 'O':
                raise ValueError('the island is not surrounded by ocean.')
        for east_coord in self.geostring_list[(self.column - 1)::self.column]:
            if east_coord != 'O':
                raise ValueError('the island is not surrounded by ocean.')

        return self.landscape, self.geostring_list

    #@classmethod
    #def island_surrounded_by_ocean:


    def populate_island(self):
        for coord in range(len(self.poplist)):
            self.loc = self.poplist[coord]['loc']  ###
            population = self.poplist[coord]['pop']
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

    Landscape = Landscape(geostring, poplist)
    landscape, geostring_list = Landscape.create_landscape()
    print(landscape)

    herb, carn = Landscape.populate_island()
    print(herb)
    print(carn)


[{'loc': (0, 0), 'lan': 'O'}, {'loc': (0, 1), 'lan': 'O'}, {'loc': (0, 2), 'lan': 'O'}, {'loc': (0, 3), 'lan': 'O'}, {'loc': (0, 4), 'lan': 'O'}, {'loc': (0, 5), 'lan': 'O'}, {'loc': (0, 6), 'lan': 'O'}, {'loc': (0, 7), 'lan': 'O'}, {'loc': (0, 8), 'lan': 'O'}, {'loc': (0, 9), 'lan': 'O'}, {'loc': (0, 10), 'lan': 'O'}, {'loc': (0, 11), 'lan': 'O'}, {'loc': (0, 12), 'lan': 'O'}, {'loc': (0, 13), 'lan': 'O'}, {'loc': (0, 14), 'lan': 'O'}, {'loc': (0, 15), 'lan': 'O'}, {'loc': (0, 16), 'lan': 'O'}, {'loc': (0, 17), 'lan': 'O'}, {'loc': (0, 18), 'lan': 'O'}, {'loc': (0, 19), 'lan': 'O'}, {'loc': (0, 20), 'lan': 'O'}, {'loc': (1, 0), 'lan': 'O'}, {'loc': (1, 1), 'lan': 'O'}, {'loc': (1, 2), 'lan': 'O'}, {'loc': (1, 3), 'lan': 'O'}, {'loc': (1, 4), 'lan': 'O'}, {'loc': (1, 5), 'lan': 'O'}, {'loc': (1, 6), 'lan': 'O'}, {'loc': (1, 7), 'lan': 'O'}, {'loc': (1, 8), 'lan': 'S'}, {'loc': (1, 9), 'lan': 'M'}, {'loc': (1, 10), 'lan': 'M'}, {'loc': (1, 11), 'lan': 'M'}, {'loc': (1, 12), 'lan': 'M'}, {'loc': (1, 13), 'lan': 'J'}, {'loc': (1, 14), 'lan': 'J'}, {'loc': (1, 15), 'lan': 'J'}, {'loc': (1, 16), 'lan': 'J'}, {'loc': (1, 17), 'lan': 'J'}, {'loc': (1, 18), 'lan': 'J'}, {'loc': (1, 19), 'lan': 'J'}, {'loc': (1, 20), 'lan': 'O'}, {'loc': (2, 0), 'lan': 'O'}, {'loc': (2, 1), 'lan': 'S'}, {'loc': (2, 2), 'lan': 'S'}, {'loc': (2, 3), 'lan': 'S'}, {'loc': (2, 4), 'lan': 'S'}, {'loc': (2, 5), 'lan': 'S'}, {'loc': (2, 6), 'lan': 'J'}, {'loc': (2, 7), 'lan': 'J'}, {'loc': (2, 8), 'lan': 'J'}, {'loc': (2, 9), 'lan': 'J'}, {'loc': (2, 10), 'lan': 'M'}, {'loc': (2, 11), 'lan': 'M'}, {'loc': (2, 12), 'lan': 'J'}, {'loc': (2, 13), 'lan': 'J'}, {'loc': (2, 14), 'lan': 'J'}, {'loc': (2, 15), 'lan': 'J'}, {'loc': (2, 16), 'lan': 'J'}, {'loc': (2, 17), 'lan': 'J'}, {'loc': (2, 18), 'lan': 'J'}, {'loc': (2, 19), 'lan': 'O'}, {'loc': (2, 20), 'lan': 'O'}, {'loc': (3, 0), 'lan': 'O'}, {'loc': (3, 1), 'lan': 'S'}, {'loc': (3, 2), 'lan': 'S'}, {'loc': (3, 3), 'lan': 'S'}, {'loc': (3, 4), 'lan': 'S'}, {'loc': (3, 5), 'lan': 'S'}, {'loc': (3, 6), 'lan': 'S'}, {'loc': (3, 7), 'lan': 'S'}, {'loc': (3, 8), 'lan': 'S'}, {'loc': (3, 9), 'lan': 'S'}, {'loc': (3, 10), 'lan': 'M'}, {'loc': (3, 11), 'lan': 'M'}, {'loc': (3, 12), 'lan': 'J'}, {'loc': (3, 13), 'lan': 'J'}, {'loc': (3, 14), 'lan': 'J'}, {'loc': (3, 15), 'lan': 'J'}, {'loc': (3, 16), 'lan': 'J'}, {'loc': (3, 17), 'lan': 'J'}, {'loc': (3, 18), 'lan': 'O'}, {'loc': (3, 19), 'lan': 'O'}, {'loc': (3, 20), 'lan': 'O'}, {'loc': (4, 0), 'lan': 'O'}, {'loc': (4, 1), 'lan': 'S'}, {'loc': (4, 2), 'lan': 'S'}, {'loc': (4, 3), 'lan': 'S'}, {'loc': (4, 4), 'lan': 'S'}, {'loc': (4, 5), 'lan': 'S'}, {'loc': (4, 6), 'lan': 'J'}, {'loc': (4, 7), 'lan': 'J'}, {'loc': (4, 8), 'lan': 'J'}, {'loc': (4, 9), 'lan': 'J'}, {'loc': (4, 10), 'lan': 'J'}, {'loc': (4, 11), 'lan': 'J'}, {'loc': (4, 12), 'lan': 'J'}, {'loc': (4, 13), 'lan': 'J'}, {'loc': (4, 14), 'lan': 'J'}, {'loc': (4, 15), 'lan': 'J'}, {'loc': (4, 16), 'lan': 'J'}, {'loc': (4, 17), 'lan': 'J'}, {'loc': (4, 18), 'lan': 'O'}, {'loc': (4, 19), 'lan': 'O'}, {'loc': (4, 20), 'lan': 'O'}, {'loc': (5, 0), 'lan': 'O'}, {'loc': (5, 1), 'lan': 'S'}, {'loc': (5, 2), 'lan': 'S'}, {'loc': (5, 3), 'lan': 'S'}, {'loc': (5, 4), 'lan': 'S'}, {'loc': (5, 5), 'lan': 'S'}, {'loc': (5, 6), 'lan': 'J'}, {'loc': (5, 7), 'lan': 'J'}, {'loc': (5, 8), 'lan': 'J'}, {'loc': (5, 9), 'lan': 'D'}, {'loc': (5, 10), 'lan': 'D'}, {'loc': (5, 11), 'lan': 'J'}, {'loc': (5, 12), 'lan': 'J'}, {'loc': (5, 13), 'lan': 'J'}, {'loc': (5, 14), 'lan': 'S'}, {'loc': (5, 15), 'lan': 'J'}, {'loc': (5, 16), 'lan': 'J'}, {'loc': (5, 17), 'lan': 'J'}, {'loc': (5, 18), 'lan': 'O'}, {'loc': (5, 19), 'lan': 'O'}, {'loc': (5, 20), 'lan': 'O'}, {'loc': (6, 0), 'lan': 'O'}, {'loc': (6, 1), 'lan': 'S'}, {'loc': (6, 2), 'lan': 'S'}, {'loc': (6, 3), 'lan': 'J'}, {'loc': (6, 4), 'lan': 'J'}, {'loc': (6, 5), 'lan': 'J'}, {'loc': (6, 6), 'lan': 'J'}, {'loc': (6, 7), 'lan': 'J'}, {'loc': (6, 8), 'lan': 'D'}, {'loc': (6, 9), 'lan': 'D'}, {'loc': (6, 10), 'lan': 'D'}, {'loc': (6, 11), 'lan': 'J'}, {'loc': (6, 12), 'lan': 'J'}, {'loc': (6, 13), 'lan': 'J'}, {'loc': (6, 14), 'lan': 'S'}, {'loc': (6, 15), 'lan': 'S'}, {'loc': (6, 16), 'lan': 'S'}, {'loc': (6, 17), 'lan': 'S'}, {'loc': (6, 18), 'lan': 'O'}, {'loc': (6, 19), 'lan': 'O'}, {'loc': (6, 20), 'lan': 'O'}, {'loc': (7, 0), 'lan': 'O'}, {'loc': (7, 1), 'lan': 'O'}, {'loc': (7, 2), 'lan': 'S'}, {'loc': (7, 3), 'lan': 'S'}, {'loc': (7, 4), 'lan': 'S'}, {'loc': (7, 5), 'lan': 'S'}, {'loc': (7, 6), 'lan': 'J'}, {'loc': (7, 7), 'lan': 'J'}, {'loc': (7, 8), 'lan': 'J'}, {'loc': (7, 9), 'lan': 'D'}, {'loc': (7, 10), 'lan': 'D'}, {'loc': (7, 11), 'lan': 'J'}, {'loc': (7, 12), 'lan': 'J'}, {'loc': (7, 13), 'lan': 'J'}, {'loc': (7, 14), 'lan': 'S'}, {'loc': (7, 15), 'lan': 'O'}, {'loc': (7, 16), 'lan': 'O'}, {'loc': (7, 17), 'lan': 'O'}, {'loc': (7, 18), 'lan': 'O'}, {'loc': (7, 19), 'lan': 'O'}, {'loc': (7, 20), 'lan': 'O'}, {'loc': (8, 0), 'lan': 'O'}, {'loc': (8, 1), 'lan': 'S'}, {'loc': (8, 2), 'lan': 'S'}, {'loc': (8, 3), 'lan': 'S'}, {'loc': (8, 4), 'lan': 'J'}, {'loc': (8, 5), 'lan': 'J'}, {'loc': (8, 6), 'lan': 'J'}, {'loc': (8, 7), 'lan': 'J'}, {'loc': (8, 8), 'lan': 'J'}, {'loc': (8, 9), 'lan': 'D'}, {'loc': (8, 10), 'lan': 'D'}, {'loc': (8, 11), 'lan': 'J'}, {'loc': (8, 12), 'lan': 'J'}, {'loc': (8, 13), 'lan': 'J'}, {'loc': (8, 14), 'lan': 'J'}, {'loc': (8, 15), 'lan': 'J'}, {'loc': (8, 16), 'lan': 'J'}, {'loc': (8, 17), 'lan': 'J'}, {'loc': (8, 18), 'lan': 'O'}, {'loc': (8, 19), 'lan': 'O'}, {'loc': (8, 20), 'lan': 'O'}, {'loc': (9, 0), 'lan': 'O'}, {'loc': (9, 1), 'lan': 'S'}, {'loc': (9, 2), 'lan': 'S'}, {'loc': (9, 3), 'lan': 'S'}, {'loc': (9, 4), 'lan': 'S'}, {'loc': (9, 5), 'lan': 'J'}, {'loc': (9, 6), 'lan': 'J'}, {'loc': (9, 7), 'lan': 'J'}, {'loc': (9, 8), 'lan': 'J'}, {'loc': (9, 9), 'lan': 'D'}, {'loc': (9, 10), 'lan': 'D'}, {'loc': (9, 11), 'lan': 'J'}, {'loc': (9, 12), 'lan': 'J'}, {'loc': (9, 13), 'lan': 'J'}, {'loc': (9, 14), 'lan': 'J'}, {'loc': (9, 15), 'lan': 'O'}, {'loc': (9, 16), 'lan': 'O'}, {'loc': (9, 17), 'lan': 'O'}, {'loc': (9, 18), 'lan': 'O'}, {'loc': (9, 19), 'lan': 'O'}, {'loc': (9, 20), 'lan': 'O'}, {'loc': (10, 0), 'lan': 'O'}, {'loc': (10, 1), 'lan': 'O'}, {'loc': (10, 2), 'lan': 'S'}, {'loc': (10, 3), 'lan': 'S'}, {'loc': (10, 4), 'lan': 'S'}, {'loc': (10, 5), 'lan': 'S'}, {'loc': (10, 6), 'lan': 'J'}, {'loc': (10, 7), 'lan': 'J'}, {'loc': (10, 8), 'lan': 'J'}, {'loc': (10, 9), 'lan': 'J'}, {'loc': (10, 10), 'lan': 'J'}, {'loc': (10, 11), 'lan': 'J'}, {'loc': (10, 12), 'lan': 'J'}, {'loc': (10, 13), 'lan': 'J'}, {'loc': (10, 14), 'lan': 'O'}, {'loc': (10, 15), 'lan': 'O'}, {'loc': (10, 16), 'lan': 'O'}, {'loc': (10, 17), 'lan': 'O'}, {'loc': (10, 18), 'lan': 'O'}, {'loc': (10, 19), 'lan': 'O'}, {'loc': (10, 20), 'lan': 'O'}, {'loc': (11, 0), 'lan': 'O'}, {'loc': (11, 1), 'lan': 'O'}, {'loc': (11, 2), 'lan': 'O'}, {'loc': (11, 3), 'lan': 'S'}, {'loc': (11, 4), 'lan': 'S'}, {'loc': (11, 5), 'lan': 'S'}, {'loc': (11, 6), 'lan': 'S'}, {'loc': (11, 7), 'lan': 'J'}, {'loc': (11, 8), 'lan': 'J'}, {'loc': (11, 9), 'lan': 'J'}, {'loc': (11, 10), 'lan': 'J'}, {'loc': (11, 11), 'lan': 'J'}, {'loc': (11, 12), 'lan': 'J'}, {'loc': (11, 13), 'lan': 'J'}, {'loc': (11, 14), 'lan': 'O'}, {'loc': (11, 15), 'lan': 'O'}, {'loc': (11, 16), 'lan': 'O'}, {'loc': (11, 17), 'lan': 'O'}, {'loc': (11, 18), 'lan': 'O'}, {'loc': (11, 19), 'lan': 'O'}, {'loc': (11, 20), 'lan': 'O'}, {'loc': (12, 0), 'lan': 'O'}, {'loc': (12, 1), 'lan': 'O'}, {'loc': (12, 2), 'lan': 'O'}, {'loc': (12, 3), 'lan': 'O'}, {'loc': (12, 4), 'lan': 'O'}, {'loc': (12, 5), 'lan': 'O'}, {'loc': (12, 6), 'lan': 'O'}, {'loc': (12, 7), 'lan': 'O'}, {'loc': (12, 8), 'lan': 'O'}, {'loc': (12, 9), 'lan': 'O'}, {'loc': (12, 10), 'lan': 'O'}, {'loc': (12, 11), 'lan': 'O'}, {'loc': (12, 12), 'lan': 'O'}, {'loc': (12, 13), 'lan': 'O'}, {'loc': (12, 14), 'lan': 'O'}, {'loc': (12, 15), 'lan': 'O'}, {'loc': (12, 16), 'lan': 'O'}, {'loc': (12, 17), 'lan': 'O'}, {'loc': (12, 18), 'lan': 'O'}, {'loc': (12, 19), 'lan': 'O'}, {'loc': (12, 20), 'lan': 'O'}]
[{'age': 10, 'weight': 15, 'loc': (3, 4)}, {'age': 5, 'weight': 40, 'loc': (3, 4)}, {'age': 15, 'weight': 25, 'loc': (3, 4)}, {'age': 2, 'weight': 60, 'loc': (4, 4)}, {'age': 9, 'weight': 30, 'loc': (4, 4)}, {'age': 16, 'weight': 14, 'loc': (4, 4)}]
[{'age': 3, 'weight': 35, 'loc': (4, 4)}, {'age': 5, 'weight': 20, 'loc': (4, 4)}, {'age': 8, 'weight': 5, 'loc': (4, 4)}]





