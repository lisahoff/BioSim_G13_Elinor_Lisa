# -*- coding: utf-8 -*-

__author__ = "Elinor Skårås og Lisa Hoff"
__email__ = "elinor2511@gmail.com, lisast@nmbu.no"



class Landscape():
    def __init__ (self, geostring):
        pass

    def create_landscape(self, geostring):
        self.geostring = geostring
        self.landscape = []
        self.geostring_split = geostring.split()
        self.column = len(geostring.split()[0])
        self.row = len(geostring.split())
        self.geostring_list = []

        for row_geostring in range(0, self.row):
            for element in self.geostring_split[row_geostring]:
                self.geostring_list.append(element)

        geostring_str = ''.join(self.geostring_list)
        n = 0
        for i in range(self.row):
            for j in range(self.column):
                coord = (i, j)
                self.landscape.append({"loc": coord, "lan": geostring_str[n]})
                n += 1

        for north_coord in self.geostring_list[:self.column]:
            if north_coord != 'O':
                raise ValueError('the island is not surrounded by ocean')
        for south_coord in self.geostring_list[self.column * (self.row - 1):]:
            if south_coord != 'O':
                raise ValueError('the island is not surrounded by ocean')
        for west_coord in self.geostring_list[0::self.column]:
            if west_coord != 'O':
                raise ValueError('the island is not surrounded by ocean')
        for east_coord in self.geostring_list[(self.column - 1)::self.column]:
            if east_coord != 'O':
                raise ValueError('the island is not surrounded by ocean')

        return self.landscape, self.geostring_list



if __name__ == "__main__":
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

    Landscape = Landscape(geostring)
    landscape, geostring_list = Landscape.create_landscape(geostring)
    print(landscape)


    print(geostring_list)


