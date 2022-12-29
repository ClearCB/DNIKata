class AssignmentTable:

    def __init__(self):
        
        self.assignment_table = ["T","R","W","A","G","M","Y","F",
                            "P","D","X","B","N","J","Z","S",
                            "Q","V","H","L","C","K","E"]

    def getLength(self):

        return len(self.assignment_table)

    def letterPosition(self, number):

        letter_position = int(number) % self.getLength()

        return letter_position

    def getLetter(self, number):

        position = self.letterPosition(number)

        try:

            return self.assignment_table[position]

        except: 

            print("The letter is not in the assignment table")

    def correctLetter(self, letter):

        return letter in self.assignment_table