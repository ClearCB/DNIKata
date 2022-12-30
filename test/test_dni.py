from src.dni import DNI
import pytest

@pytest.fixture
def dniTest():

    dni = DNI("49481746", "Y")
    return dni

@pytest.fixture
def dniTestIncorrect():

    dni_incorrect = DNI("4848*81484","Ñ")
    return dni_incorrect


@pytest.mark.test_dniConstructor
def test_dniConstructor():

    number_dni = "123456789"
    letter_dni = "D"

    dni = DNI("123456789","D")

    assert dni.dni == (number_dni + letter_dni)
    assert dni.tabla.assignment_table[9] == "D"

@pytest.mark.test_setNumber
def test_setNumber(dniTest):

    assert dniTest.number == "49481746"

    dniTest.setNumber("123123")

    assert dniTest.number == "123123"

@pytest.mark.test_setLetter
def test_setLetter(dniTest):

    dniTest.letter = "Ñ"

    assert dniTest.letter == "Ñ"

    dniTest.setLetter()

    assert dniTest.letter == "Y"

@pytest.mark.test_setDni
def test_setDni(dniTest):

    dniTest.dni = "49481746"

    assert dniTest.dni == "49481746"

    dniTest.setDni()

    assert dniTest.dni == "49481746Y"

@pytest.mark.test_letterIsCorrect
def test_letterIsCorrect(dniTest):

    assert dniTest.letterIsCorrect() == True

@pytest.mark.test_numberLengthIsCorrect
def test_numberLengthIsCorrect(dniTest,dniTestIncorrect):

    assert dniTest.numberLengthIsCorrect() == True
    assert dniTestIncorrect.numberLengthIsCorrect() == False

@pytest.mark.test_numberIsIntegrer
def test_numberIsIntegrer(dniTest,dniTestIncorrect):

    assert dniTest.numberIsIntegrer() == True
    assert dniTestIncorrect.numberIsIntegrer() == False

@pytest.mark.test_dniIsCorrect
def test_dniIsCorrect(dniTest,dniTestIncorrect):

    assert dniTest.dniIsCorrect() == True
    assert dniTestIncorrect.dniIsCorrect() == False