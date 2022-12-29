class AssignmentTable:

    def __init__(self):
        
        self.assignment_table = ["T","R","W","A","G","M","Y","F",
                            "P","D","X","B","N","J","Z","S",
                            "Q","V","H","L","C","K","E"]

    def getLetter(self, number):

        position_letter = int(number) % 23

        return self.assignment_table[position_letter]

    def correctLetter(self, letter):

        return letter in self.assignment_table