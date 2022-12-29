from src.assignmentTable import AssignmentTable
import pytest

# Test if the table can be called correclty
@pytest.mark.test_assignmentTable
def test_assignmentTable():

    table = AssignmentTable()
    first_letter = table.assignment_table[0]

    assert type(first_letter) == str

