# Aplicacion que nos permita registrar los vehiculos que ingresan/salen a un parqueadero
# Placa (Vehiculo)
# Hora de ingreso
# Lugar de parqueo
# Fecha de ingreso
# Hora de salida
# Fecha de salida
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
    
    
    
# Crear un vehiculo

# Condition of the while loop
opcion = 0
parqueadero = []
while opcion < 3 :  
    print("1. Registrar Vehiculo")
    print("2. Mostrar Vehiculo")
    print("3. Salir")

    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        placa = input("Ingrese la placa del vehiculo: ")
        color = input("Ingrese el color del vehiculo: ")
        observaciones = input("Ingrese las observaciones del vehiculo: ")
        vehiculo = Vehiculo(placa, color, observaciones)
        print(vehiculo)
        parqueadero.append(vehiculo)
    elif opcion == 2:        
        for auto in parqueadero:
            print(auto)
    elif opcion == 3:        
        print("Saliendo...")

    
    

