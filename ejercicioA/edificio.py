class Edificio:
    def __init__(self, nombre):
        self.nombre = nombre
    def __del__(self):
        print("Se ha destruido {}".format(self.nombre))
