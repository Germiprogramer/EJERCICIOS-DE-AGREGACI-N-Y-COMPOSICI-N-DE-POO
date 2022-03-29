from edificio import *

class Ciudad:
    def __init__(self,nombre, edificio):
        self.nombre = nombre
        self.edificio = edificio

NewYork = Ciudad("NewYork", [Edificio("A"), Edificio("B")])
LosAngeles = Ciudad("LosAngeles", Edificio("C"))