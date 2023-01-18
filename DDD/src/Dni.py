from src.Table import *
'''
This file will contain the class Dni that will be the main information about 
the DNI, that will be related to Table class (./Table.py)
'''

class Dni(Table):

    # Constructor
    def __init__(self, nif):

        self.dni = ''
        self.nif = nif
        self.control_digit = None
        self.letter = None
        self.assignment_table = Table()

    # Getters / Setters
    def getDni(self):

        return self.dni

    def getNif(self):

        return self.nif

    def getControlDigit(self):

        return self.control_digit

    def getLetter(self):

        return self.letter

    def setDni(self):

        self.dni = str(self.getNif()) + self.getLetter()

    def setNif(self, nif):

        self.nif = nif

    def setControlDigit(self):

        self.control_digit = (self.nif%self.assignment_table.table_length)

    def setLetter(self):

        self.letter = self.assignment_table.getCorrectLetter(self.getControlDigit())

    def __repr__(self):

        return f"Your dni is: {self.dni}"