'''
This file will contain the class Table which will have the data structure () an array
that we will use to relate the control_digit to their corresponding letter. That will 
allow us to get the full DNI. (8 int + 1 letter (str))
'''

class Table:

    def __init__(self):

        self.assignment_table = ["T","R","W","A","G","M","Y","F",
                                "P","D","X","B","N","J","Z","S",
                                "Q","V","H","L","C","K","E"]

        self.table_length = len(self.assignment_table)

    def getCorrectLetter(self, number):

        try:
            return self.assignment_table[number]
            
        except IndexError:

            return f"Sorry, the number has to be between 0 and {self.table_length}"