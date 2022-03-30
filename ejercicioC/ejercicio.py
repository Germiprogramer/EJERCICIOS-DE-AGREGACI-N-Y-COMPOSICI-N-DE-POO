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