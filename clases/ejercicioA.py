class Empresa:
    def __init__(self, nombre, edificio, empleado):
        self.nombre = nombre
        self.edificio = edificio
        self.empleado = empleado

class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre

class NuevaYork(Ciudad):
    def __init__(self):
        super().__init__()
        self