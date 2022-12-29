from src.assignmentTable import AssignmentTable

class DNI:

    def __init__(self, number):

        self.number = number
        self.tabla = AssignmentTable()

    def getLetter(self):

        return self.number[-1]

    def getNumber(self):

        return self.number[:-1]

    def letterIsCorrect(self):

        return self.getLetter() == self.tabla.correctLetter(self.getNumber())

    # def numberIsCorrect(self):

