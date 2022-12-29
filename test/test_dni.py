from src.dni import DNI
import pytest

@pytest.mark.test_dniConstructor
def test_dniConstructor():

    new_dni = "123456789D"

    dni = DNI("123456789D")

    assert dni.number == new_dni
    assert dni.tabla.assignment_table[9] == "D"
