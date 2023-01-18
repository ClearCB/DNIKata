from src.Dni import *
import pytest

'''
This module will check all the methods that the class Dni have 
'''

# We will use the fixture to start using an object as a test-sample
@pytest.fixture
def test_dni():

    test_dni_one = Dni(49481746)

    return test_dni_one

@pytest.mark.test_setControlDigit
def test_setControlDigit(test_dni):

    test_dni.setControlDigit()

    assert test_dni.control_digit == 6

@pytest.mark.test_setLetter
def test_setLetter(test_dni):

    test_dni.setControlDigit()
    test_dni.setLetter()

    assert test_dni.letter == "Y"
