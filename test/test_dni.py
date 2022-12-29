from src.dni import DNI
import pytest

@pytest.fixture
def dniTest():

    dni = DNI("49481746Y")
    return dni

@pytest.fixture
def dniTestIncorrect():

    dni_incorrect = DNI("484848484Ñ")
    return dni_incorrect


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

@pytest.mark.test_letterIsCorrect
def test_letterIsCorrect(dniTest, dniTestIncorrect):

    assert dniTest.letterIsCorrect() == True
    assert dniTestIncorrect.letterIsCorrect() == False
