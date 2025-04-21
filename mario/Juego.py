from Poder import Hongo, Planta
from Personaje import Jugador 

hongo1 = Hongo(1, "Hongo Rojo", "Hongo que hace crecer a Mario", 5, 0, "activo", "Rojo")
hongo2 = Hongo(2, "Hongo Rojo", "Hongo que hace crecer a Mario", 10, 2, "activo", "Rojo")
hongo3 = Hongo(3, "Hongo Verde", "Hongo que hace crecer a Mario", 15, 0, "activo", "Verde")

planta1 = Planta(4, "Planta Fuego", "Planta que lanza fuego", 20, 0, "activo")
mario = Jugador(1, "Mario")

def mostrarTodo():
    if(hongo1.posicionX == mario.posicionX):
        mario.recogerPoder(hongo1)
    print(mario)
    print(hongo1)
    print(hongo2)
    print(hongo3)


mario.mover(1, 0)
mario.mover(1, 0)
mario.mover(1, 0)
mario.mover(1, 0)
mostrarTodo()
mario.mover(1, 0)
mostrarTodo()


accion = 0
while accion < 5:
    print("1. Adelante")
    print("2. Atras")
    print("3. Subir")
    print("4. Bajar")
    accion = int(input("Ingrese la accion: "))
    
    if accion == 1:
       mario.mover(1, 0)
       mostrarTodo()
    elif accion == 2:
       mario.mover(-1, 0)
       mostrarTodo()
    elif accion == 3:
       mario.mover(0, 1)
       mostrarTodo()
    elif accion == 4:
        mario.mover(0, -1)
        mostrarTodo()
