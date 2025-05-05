class Personaje:
    def __init__(self, id, nombre, x, y, estado="Vivo"):
        self.id         = id
        self.nombre     = nombre
        self.posicionX  = x
        self.posicionY  = y
        self.estado     = estado

    def mover(self, dx=0, dy=0):
        self.posicionX += dx
        self.posicionY += dy

class Jugador(Personaje):
    def __init__(self, id, nombre, x=0, y=0):
        super().__init__(id, nombre, x, y)
        self.vidas   = 3
        self.monedas = 0
        self.puntos  = 0
        self.tiempo  = 300
        self.dispara = False
        self.tamano = 'pequeño'

