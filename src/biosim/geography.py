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
        self.fodder_matrix = []
        self.column = len(geostring.split)
        self.row = len(geostring.split[0])
        self.f_max_jungle = 800
        self.f_max_savanne = 300
        self.alpha_savanne = 0.3

    def create_landscape_matrix(self, geostring):
        pass

    # Husk å teste at den er omgitt av hav

    def create_fodder_matrix(self, landscape_matrix):
            for j in range(column):
                for i in range(row):
                    if geography_matrix[column][row] == 'O':
                        fodder_matrix[column][row] = None

                    if geography_matrix[column][row] == 'J':
                        fodder_matrix[column][row] = f.max_jungle

                    if geography_matrix[column][row] == 'D':
                        fodder_matrix[column][row] = None

                    if geography_matrix[column][row] == 'S':
                        fodder_matrix[column][row] = f_max_savanne

                    if geography_matrix[column][row] == 'M':
                        fodder_matrix[column][row] = None