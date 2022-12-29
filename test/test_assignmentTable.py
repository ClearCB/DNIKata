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

    dni_letter = AssignmentTable()

    assert dni_letter.getLetter("49481740") == "T"
    assert dni_letter.getLetter("49481741") == "R"
    assert dni_letter.getLetter("49481742") == "W"
    assert dni_letter.getLetter("49481743") == "A"