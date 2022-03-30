# EJERCICIOS-DE-AGREGACI-N-Y-COMPOSICI-N-DE-POO

El link al repositorio es el siguiente https://github.com/Germiprogramer/EJERCICIOS-DE-AGREGACI-N-Y-COMPOSICI-N-DE-POO.git

# EJERCICIO 1

    from persona import *
    from ciudad import *
    from edificio import *
    from empresa import *

    NewYork = Ciudad("NewYork", [Edificio("A"), Edificio("B")])
    LosAngeles = Ciudad("LosAngeles", Edificio("C"))

    Yohoo = Empresa("Yohoo", [Edificio("A"), Edificio("B"), Edificio("C")], [Persona("Martin"), Persona("Salim"), Persona("Xing")])

    del NewYork

# EJERCICIO 2

1. Al tratar de imprimir una clase, se hace la llamada al objeto.

2. Al ser yin una clase vacía, yang es igual a ying.yang

3. Se printea primero la interrogación antes que la destruccíon.

# EJERCICIO 3

    class Casa: 
        def __init__(self, pared):
            self.pared = pared

        def superficie_acristalada(self):
            return sum(self.pared.area)

    class Pared: 
        def __init__(self, ventana, orientacion):
            self.ventana = ventana
            self.orientacion = orientacion
            self.area = self.ventana.get_area()

    class Cristal:
        def __init__(self, anchuracristal):
            self.anchuracristal = anchuracristal

        def get_anchuracristal(self):
            return self.anchuracristal

    class Ventana(Cristal):
        def __init__(self, anchuracristal, area):
            super().__init__(anchuracristal)
            self.area = area


        def get_area(self):
            return self.area



    ventana1 = Ventana(2,3)
    ventana2 = Ventana(1,4)

    pared1 = Pared(ventana1, "izquierda")

    casita = Casa(pared1)

    casita.superficie_acristalada()
