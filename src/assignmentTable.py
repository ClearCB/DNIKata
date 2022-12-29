class AssignmentTable:

    def __init__(self):
        
        self.assignment_table = ["T","R","W","A","G","M","Y","F",
                            "P","D","X","B","N","J","Z","S",
                            "Q","V","H","L","C","K","E"]

    def getLetter(self, DNI):

        position_letter = int(DNI) % 23

        return self.assignment_table[position_letter]