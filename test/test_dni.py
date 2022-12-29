from src.dni import DNI
import pytest

@pytest.fixture
def dniTest():

    dni = DNI("49481746Y")
    return dni


@pytest.mark.test_dniConstructor
def test_dniConstructor():

    number_dni = "123456789"
    letter_dni = "D"

    dni = DNI("123456789D")

    assert dni.number == (number_dni + letter_dni)
    assert dni.tabla.assignment_table[9] == "D"

@pytest.mark.test_getNumber
def test_getNumber(dniTest):

    assert dniTest.getNumber() == "49481746"


@pytest.mark.test_getLetter
def test_getLetter(dniTest):

    assert dniTest.getLetter() == "Y"
