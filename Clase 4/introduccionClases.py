# Aplicacion que nos permita registrar los vehiculos que ingresan/salen a un parqueadero
# Placa (Vehiculo)

# Observaciones (Vehiculo)
# Marca (Vehiculo)
# Modelo (Vehiculo)
# Color (Vehiculo)
# #

# Definicion de la clase Vehiculo
class Vehiculo:    
    placa: str
    color: str
    velocidad: int
    observaciones: str
    
    #Set Metodo
    def __init__(self, placa, color, observaciones):
        self.placa = placa
        self.color = color
        self.observaciones = observaciones
        self.velocidad = 0

    #Get Obtener
    def __str__(self):
        return f"Vehiculo (placa={self.placa}, color={self.color} y tiene observaciones={self.observaciones})"
    
    def setVelocidad(self, velocidad):
        self.velocidad = velocidad
    
    def getVelocidad(self):
        return self.velocidad
    
    def setAcelerar(self, acelerar=10):
        self.velocidad += acelerar
        if self.velocidad < 0:
            self.velocidad = 0
    
# Crear un vehiculo

# Condition of the while loop
opcion = 0
while opcion < 4 :  
    print("1. Registrar Vehiculo")
    print("2. Acelerar vehiculo")
    print("3. Frenar vehiculo")
    print("4. Salir")

    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        placa = input("Ingrese la placa del vehiculo: ")
        color = input("Ingrese el color del vehiculo: ")
        observaciones = input("Ingrese las observaciones del vehiculo: ")
        vehiculo = Vehiculo(placa, color, observaciones)
        print(vehiculo)
        
    elif opcion == 2:        
        vehiculo.setAcelerar()
        print(f"La velocidad del vehiculo es {vehiculo.getVelocidad()}")
    elif opcion == 3:
        vehiculo.setAcelerar(-10)
        print(f"La velocidad del vehiculo es {vehiculo.getVelocidad()}")
    elif opcion == 4:
        print("Saliendo...")

    
    

