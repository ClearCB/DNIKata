from src.assignmentTable import AssignmentTable
import pytest

def tableTest():

    table = AssignmentTable()

    return table

table = tableTest()

# Test if the table can be called correclty
@pytest.mark.test_assignmentTable
def test_assignmentTable():

    first_letter = table.assignment_table[0]

    assert type(first_letter) == str

# Test if the length can be calculated correctly
@pytest.mark.test_getLenght
def test_getLenght():

    table = AssignmentTable()
    table.assignment_table = [1,2,3,4,5,6]

    assert table.getLength() == 6

    new_table = AssignmentTable()
    new_table.assignment_table = [0]

    assert new_table.getLength() == 1


# Test if we can check if a letter is correct or not
@pytest.mark.test_letterCorrect
def test_letterCorrect():

    table = AssignmentTable()

    assert table.correctLetter("Ñ") == False
    assert table.correctLetter("I") == False

# Test if we can take the position of the letter in table
@pytest.mark.test_getLetter
def test_getLetter():

    dni_letter = table

    assert dni_letter.getLetter("49481740") == "T"
    assert dni_letter.getLetter("49481741") == "R"
    assert dni_letter.getLetter("49481742") == "W"
    assert dni_letter.getLetter("49481743") == "A"

# Test if we can get the position correctly
@pytest.mark.test_getPosition
def test_getPosition():

    assert table.letterPosition("24") == 1
    assert table.letterPosition("48") == 2
    assert table.letterPosition("49481740") == 0