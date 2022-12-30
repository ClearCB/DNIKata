from src.dni import DNI
import pytest

@pytest.fixture
def dniTest():

    dni = DNI("49481746Y")
    return dni

@pytest.fixture
def dniTestNoLetter():

    dni = DNI("49481746")
    return dni

@pytest.fixture
def dniTestIncorrect():

    dni_incorrect = DNI("4848*81484Ñ")
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

@pytest.mark.test_setDni
def test_setDni(dniTestNoLetter):

    assert dniTestNoLetter.number == "49481746"

    dniTestNoLetter.setDni()

    assert dniTestNoLetter.number == "49481746Y"


@pytest.mark.test_getLetter
def test_getLetter(dniTest):

    assert dniTest.getLetter() == "Y"
    
    dniTest.number = "4948471" 

    assert dniTest.getLetter() == False


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