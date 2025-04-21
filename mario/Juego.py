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