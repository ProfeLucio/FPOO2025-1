#Clase que define los poderes que puede recoger los jugadores de mario bros
class Poder:
    id: int
    nombre: str
    descripcion: str
    posicionX: int
    posicionY: int
    estado: str

    def __init__(self, id, nombre, descripcion, posicionX, posicionY, estado):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.estado = estado
     
    def __str__(self):
        return f"Poder (nombre={self.nombre}, descripcion={self.descripcion}, posicionX={self.posicionX}, posicionY={self.posicionY})"
    
    def setEstado(self, estado):
        self.estado = estado
        print(f"El poder {self.nombre} ha cambiado su estado a {self.estado}")

class Hongo(Poder):
    tipo: str 
    def __init__(self, id, nombre, descripcion, posicionX, posicionY, estado, tipo):
        super().__init__(id, nombre, descripcion, posicionX, posicionY, estado)
        self.tipo = tipo
    
        
    def mover(self, x=0, y=0):
        self.posicionX += x
        self.posicionY += y
        print(f"El hongo se ha movido a la posicion ({self.posicionX}, {self.posicionY})")


class Planta(Poder):
    def __init__(self, id, nombre, descripcion, posicionX, posicionY, estado):
        super().__init__(id, nombre, descripcion, posicionX, posicionY, estado)
    
    def __str__(self):
        return f"Hongo (tipo={self.tipo}, descripcion={self.descripcion}, id={self.id})"
    
