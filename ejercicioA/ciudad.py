from edificio import *

class Ciudad:
    def __init__(self, nombre, edificio):
        self.nombre = nombre
        self.edificio = edificio
    
    def __del__(self):
        print("Se ha destruido {}".format(self.nombre))
        