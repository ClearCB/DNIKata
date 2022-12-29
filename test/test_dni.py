from src.dni import DNI
import pytest

@pytest.mark.test_dniConstructor
def test_dniConstructor():

    new_dni = "123456789"

    dni = DNI("123456789")

    assert dni.number == new_dni