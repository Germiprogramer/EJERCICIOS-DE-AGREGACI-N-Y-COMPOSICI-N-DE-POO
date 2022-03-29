from persona import *
from ciudad import *
from edificio import *
from empresa import *

NewYork = Ciudad("NewYork", [Edificio("A"), Edificio("B")])
LosAngeles = Ciudad("LosAngeles", Edificio("C"))

Yohoo = Empresa("Yohoo", [Edificio("A"), Edificio("B"), Edificio("C")], [Persona("Martin"), Persona("Salim"), Persona("Xing")])

del NewYork