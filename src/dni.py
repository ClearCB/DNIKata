from src.assignmentTable import AssignmentTable

class DNI:

    def __init__(self, number, letter=""):

        self.number = number
        self.letter = letter
        self.dni = number + letter
        self.tabla = AssignmentTable()

    def setNumber(self, number):

        self.number = number

    def setLetter(self):

        self.letter = self.tabla.correctLetter(self.number)

    def setDni(self):

        self.dni = (self.number + self.tabla.correctLetter(self.number))

    def letterIsCorrect(self):

        try:
            return self.letter == self.tabla.correctLetter(self.number)
        except:
            return False

    def numberLengthIsCorrect(self):

        return len(self.number) == 8

    def numberIsIntegrer(self):

        try:
            int(self.number)
            return True

        except:
            return False 

    def dniIsCorrect(self):

        return self.numberLengthIsCorrect() and self.numberIsIntegrer() and self.letterIsCorrect()


if __name__ == "__main__":

    dni = DNI("494")

    print(dni.dni)

    dni.setDni()

    print(dni.dni)

    print(dni.dniIsCorrect())

    dni.setNumber("49481746")
    dni.setDni()

    print(dni.dni)