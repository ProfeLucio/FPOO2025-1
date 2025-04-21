#Los personajes del Juego tanto Jugador como enemigos
from Poder import Hongo, Planta
class Personaje:
    id: int
    nombre: str
    posicionX: int
    posicionY: int
    estado: str 

    def __init__(self, id, nombre, posicionX, posicionY, estado):
        self.id = id
        self.nombre = nombre
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.estado = estado

    def __str__(self):
        return f"Personaje ({self.nombre}, {self.posicionX}, {self.posicionY})"
    
    def mover(self, x=0, y=0):
        self.posicionX += x
        self.posicionY += y
        print(f"El personaje {self.nombre} se ha movido a la posicion ({self.posicionX}, {self.posicionY})")

class Jugador(Personaje):
    vidas: int
    tamano: str
    dispara: bool = False
    monedas: int
    puntos: int
    tiempo: int
    estado: str

    def __init__(self, id, nombre):
        super().__init__(id, nombre, 0, 0, "Vivo")
        self.vidas = 3
        self.tamano = "enano"
        self.monedas = 0
        self.puntos = 0
        self.tiempo = 300
    
    def __str__(self):
        return f" ({self.nombre}, {self.posicionX}, {self.posicionY}, {self.tamano})"

    def recogerPoder(self, poder):
        if isinstance(poder, Hongo):
            if poder.tipo == "Rojo":
                self.tamano = "grande"
            elif poder.tipo == "Verde":
                self.vidas += 1
            poder.setEstado("recogido")
            print(f"El jugador {self.nombre} ha recogido el poder {poder.nombre}")
        elif isinstance(poder, Planta):
            self.dispara = True
            poder.setEstado("recogido")
            print(f"El jugador {self.nombre} ha recogido el poder {poder.nombre}")
        else:
            print("Poder no reconocido")