class AssignmentTable:

    def __init__(self):
        
        self.assignment_table = ["T","R","W","A","G","M","Y","F",
                            "P","D","X","B","N","J","Z","S",
                            "Q","V","H","L","C","K","E"]

    def getLength(self):

        return len(self.assignment_table)

    def getLetter(self, number):

        try:

            letter_in_table = self.assignment_table[int(number) % self.getLength()]
            return letter_in_table

        except IndexError:

            print("The letter is not in the assignment table")

    def correctLetter(self, letter):

        return letter in self.assignment_table