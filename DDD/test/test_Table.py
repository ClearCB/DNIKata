from src.Table import *
import pytest

'''
At this file we will test the class table and check if the table can be 
consulted and return the letter correctly.
'''

@pytest.fixture
def test_table():

    test_table_one = Table()

    return test_table_one

@pytest.mark.test_getCorrectLetter
def test_getCorrectLetter(test_table):

    assert test_table.getCorrectLetter(500) == 'Sorry, the number has to be between 0 and 23'
    assert test_table.getCorrectLetter(6) == "Y"
    assert test_table.getCorrectLetter(22) == "E"