from src.assignmentTable import AssignmentTable
import pytest

# Creating a function to call the class always the same sintax, so we can use each time we need
@pytest.fixture
def tableTest():

    table = AssignmentTable()

    return table

# Test if the table can be called and created correctly
@pytest.mark.test_assignmentTable
def test_assignmentTable(tableTest):

    assert type(tableTest.assignment_table[0]) == str

# Test if the length can be calculated correctly
@pytest.mark.test_getLenght
def test_getLenght(tableTest):

    # Reasignment of the length
    tableTest.assignment_table = [1,2,3,4,5,6]

    assert tableTest.getLength() == 6

    tableTest.assignment_table = [0]

    assert tableTest.getLength() == 1

# Test if we can get the position correctly
@pytest.mark.test_letterPosition
def test_letterPosition(tableTest):


    assert tableTest.letterPosition("24") == 1
    assert tableTest.letterPosition("48") == 2
    assert tableTest.letterPosition("49481740") == 0

# Test if we can take the position of the letter in table
@pytest.mark.test_correctLetter
def test_correctLetter(tableTest):

    assert tableTest.correctLetter("49481740") == "T"
    assert tableTest.correctLetter("49481741") == "R"
    assert tableTest.correctLetter("49481742") == "W"
    assert tableTest.correctLetter("49481743") == "A"

# Test if we can check if a letter is correct or not
@pytest.mark.test_letterIsUp
def test_letterIsUp(tableTest):

    assert tableTest.letterIsUp("Ñ") == False
    assert tableTest.letterIsUp("I") == False