class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def __del__(self):
        print("Ha muerto {}".format(self.nombre))
