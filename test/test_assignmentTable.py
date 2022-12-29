from src.assignmentTable import AssignmentTable
import pytest

# Creating a function to call the class always the same sintax, so we can use each time we need
def tableTest():

    table = AssignmentTable()

    return table

# Test if the table can be called and created correctly
@pytest.mark.test_assignmentTable
def test_assignmentTable():

    first_letter = tableTest().assignment_table[0]

    assert type(first_letter) == str


# Test if the length can be calculated correctly
@pytest.mark.test_getLenght
def test_getLenght():

    # Reasignment of the length
    table = tableTest()
    table.assignment_table = [1,2,3,4,5,6]

    assert table.getLength() == 6

    new_table = tableTest()
    new_table.assignment_table = [0]

    assert new_table.getLength() == 1

# Test if we can get the position correctly
@pytest.mark.test_letterPosition
def test_letterPosition():

    table = tableTest()

    assert table.letterPosition("24") == 1
    assert table.letterPosition("48") == 2
    assert table.letterPosition("49481740") == 0

# Test if we can take the position of the letter in table
@pytest.mark.test_getLetter
def test_getLetter():

    dni_letter = tableTest()

    assert dni_letter.getLetter("49481740") == "T"
    assert dni_letter.getLetter("49481741") == "R"
    assert dni_letter.getLetter("49481742") == "W"
    assert dni_letter.getLetter("49481743") == "A"

# Test if we can check if a letter is correct or not
@pytest.mark.test_letterCorrect
def test_letterCorrect():

    table = tableTest()

    assert table.correctLetter("Ñ") == False
    assert table.correctLetter("I") == False



