class AssignmentTable:

    def __init__(self):
        
        self.assignment_table = ["T","R","W","A","G","M","Y","F",
                            "P","D","X","B","N","J","Z","S",
                            "Q","V","H","L","C","K","E"]

    # This method return the lenght of the table assigned
    def getLength(self):

        return len(self.assignment_table)

    # This method takes the position in the table with the number given
    def letterPosition(self, number):

        return int(number) % self.getLength()

    # This method takes the letter in the table
    def correctLetter(self, number):

        return self.assignment_table[self.letterPosition(number)]

    # This method check if the letter given is in the table
    def letterIsUp(self, letter):

        return letter.upper() in self.assignment_table