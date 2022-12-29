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

    def numberLengthIsCorrect(self):

        return len(self.getNumber()) == 8

    def numberIsIntegrer(self):

        try:
            int(self.getNumber())
            return True

        except:
            return False 

    def dniIsCorrect(self):

        try:
            return self.numberLengthIsCorrect() and self.numberIsIntegrer() and self.letterIsCorrect()
        except:
            return False


if __name__ == "__main__":

    dniCorrect = DNI("49481746Y")

    dniIncorrectLength = DNI("123456789L")

    dniIncorrectLetter = DNI("12345678Ñ")

    print(dniCorrect.dniIsCorrect())
    print(dniIncorrectLength.dniIsCorrect())
    print(dniIncorrectLetter.dniIsCorrect())