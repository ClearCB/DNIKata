from src.assignmentTable import AssignmentTable
import pytest

# Test if the table can be called correclty
@pytest.mark.test_assignmentTable
def test_assignmentTable():

    table = AssignmentTable()
    first_letter = table.assignment_table[0]

    assert type(first_letter) == str

# Test if we can take the position of the letter in table
@pytest.mark.test_getLetter
def test_getLetter():

    dni = '49481740'

    dni_letter = AssignmentTable()

    assert dni_letter.getLetter(dni) == "T"