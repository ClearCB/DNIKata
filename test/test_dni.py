from src.dni import DNI
import pytest

@pytest.mark.test_dniConstructor
def test_dniConstructor():

    number_dni = "123456789"
    letter_dni = "D"

    dni = DNI("123456789D")

    assert dni.number == (number_dni + letter_dni) 
    assert dni.tabla.assignment_table[9] == "D"
