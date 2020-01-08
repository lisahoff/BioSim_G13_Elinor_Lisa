# -*- coding: utf-8 -*-

__author__ = "Elinor skaras og Lisa Hoff"
__email__ = "elinor9511@gmail.com, lisast@nmbu.no"


class Create_landscape(object):
    '''
    The landscape of the island.
    '''

    def __init__(self, geostring):
        self.geostring = geostring
        self.landscape_matrix = []
        self.f_max_jungle = 800
        self.f_max_savanne = 300
        self.alpha_savanne = 0.3
        self.geostring_split = geostring.split()

    def create_landscape_matrix(self, geostring):
        geostring_split = geostring.split()

        column = len(geostring_split[0])
        row = len(geostring_split)

        geostring_list = []

        for row_geostring in range(0, row):
            for element in geostring_split[row_geostring]:
                geostring_list.append(element)

        landscape_matrix = [[0 for i in range(column)] for j in range(row)]

        n = 0
        for i in range(row):
            for j in range(column):
                value = geostring_list[n]
                landscape_matrix[i][j] = value
                n += 1
        return landscape_matrix

    # Husk å teste at den er omgitt av hav

    def create_fodder_matrix(self, landscape_matrix):
        geostring_split = geostring.split()

        column = len(geostring_split[0])
        row = len(geostring_split)
        fodder_matrix = [[0 for i in range(column)] for j in range(row)]

        for i in range(row):
            for j in range(column):
                if landscape_matrix[i][j] == 'O':
                    fodder_matrix[i][j] = None
                if landscape_matrix[i][j] == 'J':
                    fodder_matrix[i][j] = self.f_max_jungle

                if landscape_matrix[i][j] == 'D':
                    fodder_matrix[i][j] = None
                if landscape_matrix[i][j] == 'S':
                    fodder_matrix[i][j] = self.f_max_savanne

                if landscape_matrix[i][j] == 'M':
                    fodder_matrix[i][j] = None
        return fodder_matrix


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

    geo = Create_landscape(geostring)

    landscape = geo.create_landscape_matrix(geostring)
    fodder = geo.create_fodder_matrix(landscape)