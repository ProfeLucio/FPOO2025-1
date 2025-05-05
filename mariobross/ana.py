
import tkinter as tk
from PIL import Image, ImageTk
import random

# Constantes
PASO_X = 10
JUMP_HEIGHT = 100
JUMP_STEPS = 10

class Personaje:
    def __init__(self, id, nombre, x, y, estado="Vivo"):
        self.id = id
        self.nombre = nombre
        self.posicionX = x
        self.posicionY = y
        self.estado = estado

def mover(self, dx=0, dy=0):
    self.posicionX += dx
    self.posicionY += dy

class Jugador(Personaje):
    def __init__(self, id, nombre, x=0, y=0):
        super().__init__(id, nombre, x, y)
        self.vidas = 3
        self.monedas = 0
        self.puntos = 0
        self.tiempo = 300
        self.dispara = False

class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Juego con Hongos")
        self.menu = tk.Frame(self.root)
        tk.Label(self.menu, text="Mi Juego", font=("Arial", 24)).pack(pady=20)
        tk.Button(self.menu, text="Iniciar", command=self.start_game).pack()
        self.menu.pack(fill="both", expand=True)

        self.ancho = 500
        self.alto = 400
        self.canvas = tk.Canvas(self.root, width=self.ancho, height=self.alto)

        self.imgs = {}
        self.load_images()

        self.players = []
        self.stats_texts = {}

        self.root.bind("<Key>", self.on_key)

def load_images(self):
    fondo = Image.open("fondo.jpeg").resize((self.ancho, self.alto))
    self.imgs["fondo"] = ImageTk.PhotoImage(fondo)

    base = Image.open("1.png").resize((50, 50))
    base_i = Image.open("1i.png").resize((50, 50))
    izq = Image.open("2i.png").resize((50, 50))
    der = Image.open("2.png").resize((50, 50))
    self.imgs["inicial"] = ImageTk.PhotoImage(base)
    self.imgs["inicialI"] = ImageTk.PhotoImage(base_i)
    self.imgs["izquierda"]= ImageTk.PhotoImage(izq)
    self.imgs["derecha"] = ImageTk.PhotoImage(der)

    hongo_crecimiento = Image.open("hongo de crecimiento.png").resize((40, 40))
    self.imgs["hongo"] = ImageTk.PhotoImage(hongo_crecimiento)

    hongo_vida = Image.open("hongo de vida.png").resize((40, 40))
    self.imgs["vida"] = ImageTk.PhotoImage(hongo_vida)

def start_game(self):
    self.menu.destroy()
    self.canvas.pack()
    self.canvas.create_image(0, 0, anchor="nw", image=self.imgs["fondo"])

    p1 = Jugador(1, "Jugador1", self.ancho // 2, self.alto // 2)
    self.add_player(p1, "inicial")

    self.hongo = self.canvas.create_image(250, self.alto // 2, image=self.imgs["hongo"])
    self.spawn_vida_hongo()

    self.msg_text = self.canvas.create_text(self.ancho // 2, 20, text="", font=("Arial", 16), fill="green")

    def add_player(self, p, img_key):
        pid = self.canvas.create_image(p.posicionX, p.posicionY, image=self.imgs[img_key])
        p.canvas_id = pid
        self.players.append(p)

txts = {}
x0 = 10 + (p.id - 1) * 150
for i, attr in enumerate(("posicionX", "posicionY", "vidas", "monedas", "puntos", "tiempo")):
txts[attr] = self.canvas.create_text(x0, 10 + i * 20, anchor="nw",
text=f"{attr}: {getattr(p, attr)}")
self.stats_texts[p.id] = txts

def update_stats(self, p):
for attr, tid in self.stats_texts[p.id].items():
self.canvas.itemconfig(tid, text=f"{attr}: {getattr(p, attr)}")

def on_key(self, ev):
if not self.players:
return
p = self.players[0]
k = ev.keysym
if k == "Right":
self.canvas.itemconfig(p.canvas_id, image=self.imgs["derecha"])
p.mover(dx=PASO_X)
self.canvas.move(p.canvas_id, PASO_X, 0)
self.root.after(100, lambda: self.canvas.itemconfig(p.canvas_id, image=self.imgs["inicial"]))
elif k == "Left":
self.canvas.itemconfig(p.canvas_id, image=self.imgs["izquierda"])
p.mover(dx=-PASO_X)
self.canvas.move(p.canvas_id, -PASO_X, 0)
self.root.after(100, lambda: self.canvas.itemconfig(p.canvas_id, image=self.imgs["inicialI"]))
elif k == "Up":
self.jump(p)

self.update_stats(p)

self.check_collisions(p)

def check_collisions(self, p):
coords_p = self.canvas.coords(p.canvas_id)

if hasattr(self, "hongo"):
coords_h = self.canvas.coords(self.hongo)
if abs(coords_p[0] - coords_h[0]) < 30 and abs(coords_p[1] - coords_h[1]) < 30:
self.canvas.delete(self.hongo)
del self.hongo
self.crecer_personaje(p)
self.show_message("¡Comiste hongo de crecimiento!")

if hasattr(self, "hongo_vida"):
coords_v = self.canvas.coords(self.hongo_vida)
if abs(coords_p[0] - coords_v[0]) < 30 and abs(coords_p[1] - coords_v[1]) < 30:
self.canvas.delete(self.hongo_vida)
del self.hongo_vida
p.vidas += 1
self.update_stats(p)
self.show_message("¡Comiste hongo de vida!")

def jump(self, p):
paso = JUMP_HEIGHT // JUMP_STEPS

def subir(i=0):
if i < JUMP_STEPS:
p.mover(dy=-paso)
self.canvas.move(p.canvas_id, 0, -paso)
self.update_stats(p)
self.root.after(20, lambda: subir(i + 1))
else:
bajar()

def bajar(i=0):
if i < JUMP_STEPS:
p.mover(dy=paso)
self.canvas.move(p.canvas_id, 0, paso)
self.update_stats(p)
self.root.after(20, lambda: bajar(i + 1))

subir()

def crecer_personaje(self, p):
img_grande = Image.open("4.png").resize((70, 70))
self.imgs["grande"] = ImageTk.PhotoImage(img_grande)
self.canvas.itemconfig(p.canvas_id, image=self.imgs["grande"])
p.vidas += 1
p.puntos += 100
self.update_stats(p)

def spawn_vida_hongo(self):
x = random.randint(50, self.ancho - 50)
y = random.randint(100, self.alto - 50)
self.hongo_vida = self.canvas.create_image(x, y, image=self.imgs["vida"])

def show_message(self, text):
self.canvas.itemconfig(self.msg_text, text=text)
self.root.after(2000, lambda: self.canvas.itemconfig(self.msg_text, text=""))

def run(self):
self.root.mainloop()

if __name__ == "__main__":
game = Game()
game.run()
