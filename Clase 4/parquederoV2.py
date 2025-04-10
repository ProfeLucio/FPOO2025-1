# Aplicacion que nos permita registrar los vehiculos que ingresan/salen a un parqueadero
# Placa (Vehiculo)
# Hora de ingreso
# Lugar de parqueo
# Fecha de ingreso
# Hora de salida
# Fecha de salida
# Observaciones (Vehiculo)
# Marca (Vehiculo) = id, nombre,
# Modelo (Vehiculo) = id, nombre, marca
# Color (Vehiculo)
# #
 
# Definicion de la clase Vehiculo
class Vehiculo:    
    id: int
    idmodelo: int
    placa: str
    color: str
    velocidad: int
    observaciones: str
    
    #Set Metodo
    def __init__(self, placa, color, observaciones, idmodelo):
        self.placa = placa
        self.color = color
        self.observaciones = observaciones
        self.velocidad = 0
        self.idmodelo = idmodelo

    #Get Obtener
    def __str__(self):
        return f"Vehiculo (placa={self.placa}, color={self.color} y tiene observaciones={self.observaciones})"
    
class Marca:
    id: int
    nombre: str

    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def __str__(self):
        return f"Marca: id={self.id}  nombre={self.nombre} "

class Modelo:
    id: int
    idmarca: int
    nombre: str

    def __init__(self, id, nombre, idmarca):
        self.id = id
        self.nombre = nombre
        self.idmarca = idmarca

    def __str__(self):
        return f"Modelo: nombre={self.id}  nombre={self.nombre}  marca={self.idmarca} "
    
# Crear un vehiculo

# Condition of the while loop
opcion = 0
parqueadero = []
marcas = []
modelos = []
while opcion < 7 :  
    print("1. Registrar Marca")
    print("2. Mostrar Marca")
    print("3. Registrar Modelo")
    print("4. Mostrar Modelo")
    print("5. Registrar Vehiculo")
    print("6. Mostrar Vehiculo")
    print("7. Salir")

    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        nombreMarca = input("Nombre de la Marca: ")        
        idmarca = len(marcas) + 1
        marca = Marca(idmarca, nombreMarca)
        marcas.append(marca)
    elif opcion == 2:        
        for item in marcas:
            print(item)
    #Crear Modelo
    elif opcion == 3:
        if( len(marcas) > 0):            
            print("Marcas disponibles:")
            for item in marcas:
                print(item)
            idmarca = int(input("Ingrese el id de la marca: "))
            
            
            nombreModelo = input("Nombre del Modelo: ")        
            idmodelo = len(modelos) + 1
            


            modelo = Modelo(idmodelo, nombreModelo, idmarca)
            modelos.append(modelo)
        else:
            print("No hay marcas registradas")

    elif opcion == 4:        
        for item2 in modelos:
            print(item2)
            for item3 in marcas:
                if item2.idmarca == item3.id:
                    print(item3)

    if opcion == 5:
        placa = input("Ingrese la placa del vehiculo: ")
        color = input("Ingrese el color del vehiculo: ")
        observaciones = input("Ingrese las observaciones del vehiculo: ")
        vehiculo = Vehiculo(placa, color, observaciones)
        print(vehiculo)
        parqueadero.append(vehiculo)
    elif opcion == 6:        
        for auto in parqueadero:
            print(auto)
    elif opcion == 7:        
        print("Saliendo...")

    
    

