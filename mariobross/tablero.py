import tkinter as tk
from PIL import Image, ImageTk

# Constantes
PASO_X      = 10
JUMP_HEIGHT = 100
JUMP_STEPS  = 10

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

class Game:
    def __init__(self):
        # --- Ventana y menú ---
        self.root = tk.Tk()
        self.root.title("Juego en Clases")

        self.menu = tk.Frame(self.root)
        tk.Label(self.menu, text="Mi Juego", font=("Arial",24)).pack(pady=20)
        tk.Button(self.menu, text="Iniciar", command=self.start_game).pack()
        self.menu.pack(fill="both", expand=True)

        # Preparo canvas, pero lo mostraré en start_game()
        self.ancho = 500; self.alto = 400
        self.canvas = tk.Canvas(self.root, width=self.ancho, height=self.alto, bg="white")

        # Cargo sprites
        self.imgs = {}
        self.load_images()

        # Lista de jugadores y sus textos de stats
        self.players = []
        self.stats_texts = {}

        # Teclado
        self.root.bind("<Key>", self.on_key)

    def load_images(self):
        base   = Image.open("1.png").resize((50,50))
        base_i = Image.open("1i.png").resize((50,50))
        izq    = Image.open("2i.png").resize((50,50))
        der    = Image.open("2.png").resize((50,50))
        self.imgs["inicial"]  = ImageTk.PhotoImage(base)
        self.imgs["inicialI"] = ImageTk.PhotoImage(base_i)
        self.imgs["izquierda"]= ImageTk.PhotoImage(izq)
        self.imgs["derecha"]  = ImageTk.PhotoImage(der)

    def start_game(self):
        # destruyo menú, muestro canvas y creo jugadores
        self.menu.destroy()
        self.canvas.pack(pady=20)

        p1 = Jugador(1, "Jugador1", self.ancho//2, self.alto//2)
        self.add_player(p1, "inicial")

    def add_player(self, p, img_key):
        # sprite
        pid = self.canvas.create_image(p.posicionX, p.posicionY, image=self.imgs[img_key])
        p.canvas_id = pid
        self.players.append(p)

        # stats
        txts = {}
        x0 = 10 + (p.id-1)*150
        for i, attr in enumerate(("posicionX","posicionY","vidas","monedas","puntos","tiempo")):
            txts[attr] = self.canvas.create_text(
                x0, 10 + i*20, anchor="nw",
                text=f"{attr}: {getattr(p,attr)}"
            )
        self.stats_texts[p.id] = txts

    def update_stats(self, p):
        for attr, tid in self.stats_texts[p.id].items():
            self.canvas.itemconfig(tid, text=f"{attr}: {getattr(p,attr)}")

    def on_key(self, ev):
        if not self.players: return
        p = self.players[0]
        k = ev.keysym
        if k == "Right":
            self.canvas.itemconfig(p.canvas_id, image=self.imgs["derecha"])
            p.mover(dx=PASO_X)
            self.canvas.move(p.canvas_id, PASO_X, 0)
            self.root.after(100, lambda:
                self.canvas.itemconfig(p.canvas_id, image=self.imgs["inicial"])
            )
        elif k == "Left":
            self.canvas.itemconfig(p.canvas_id, image=self.imgs["izquierda"])
            p.mover(dx=-PASO_X)
            self.canvas.move(p.canvas_id, -PASO_X, 0)
            self.root.after(100, lambda:
                self.canvas.itemconfig(p.canvas_id, image=self.imgs["inicialI"])
            )
        elif k == "Up":
            self.jump(p)
        self.update_stats(p)

    def jump(self, p):
        paso = JUMP_HEIGHT // JUMP_STEPS
        def subir(i=0):
            if i < JUMP_STEPS:
                p.mover(dy=-paso)
                self.canvas.move(p.canvas_id, 0, -paso)
                self.update_stats(p)
                self.root.after(20, lambda: subir(i+1))
            else:
                bajar()
        def bajar(i=0):
            if i < JUMP_STEPS:
                p.mover(dy=paso)
                self.canvas.move(p.canvas_id, 0, paso)
                self.update_stats(p)
                self.root.after(20, lambda: bajar(i+1))
        subir()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = Game()
    game.run()
