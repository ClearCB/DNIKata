from src.Dni import *
from src.Table import * 


if __name__ == "__main__":
        
    nif = input("Please, write your nif: ")

    dni = Dni(int(nif))

    dni.setControlDigit()
    dni.setLetter()
    dni.setDni()

    print (dni)