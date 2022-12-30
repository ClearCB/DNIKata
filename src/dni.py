from src.assignmentTable import AssignmentTable

class DNI:

    def __init__(self, number, letter=""):

        self.number = number
        self.letter = letter
        self.dni = number + letter
        self.tabla = AssignmentTable()

    def getLetter(self):

        return self.letter

    def getNumber(self):

        return self.number

    def getDni(self):

        return self.dni

    def letterIsCorrect(self):

        try:
            return self.getLetter() == self.tabla.correctLetter(self.getNumber())
        except:
            return False

    def numberLengthIsCorrect(self):

        return len(self.getNumber()) == 8

    def numberIsIntegrer(self):

        try:
            int(self.getNumber())
            return True

        except:
            return False 

    def dniIsCorrect(self):

        return self.numberLengthIsCorrect() and self.numberIsIntegrer() and self.letterIsCorrect()

    def setDni(self):

        self.number = (self.number + self.tabla.correctLetter(self.number))


if __name__ == "__main__":

    dniCorrect = DNI("49481746Y")

    dniIncorrectLength = DNI("123456789L")

    dniIncorrectLetter = DNI("12345678Ñ")

    print(dniCorrect.dniIsCorrect())
    print(dniIncorrectLength.dniIsCorrect())
    print(dniIncorrectLetter.dniIsCorrect())