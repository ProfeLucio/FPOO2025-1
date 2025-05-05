# Lógica de Negocio
import random
import tkinter as tk # pygame
from PIL import Image, ImageTk
from Personaje import Jugador

# Constantes
PASO_X      = 10
JUMP_HEIGHT = 100
JUMP_STEPS  = 10

class Game:
    def __init__(self):
        # --- Ventana y menú ---
        self.root = tk.Tk()
        self.root.title("Juego de Mario")

        self.menu = tk.Frame(self.root)
        tk.Label(self.menu, text="Mi Juego", font=("Arial",24)).pack(pady=20)
        tk.Button(self.menu, text="Iniciar", command=self.start_game).pack()
        self.menu.pack(fill="both", expand=True)

        # Preparo canvas, pero lo mostraré en start_game()
        self.ancho = 800; self.alto = 400
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
        inicial   = Image.open("1.png").resize((50,50))
        inicialGrande = Image.open("1.png").resize((60,60))
        base_i = Image.open("1i.png").resize((50,50))
        izq    = Image.open("2i.png").resize((50,50))
        der    = Image.open("2.png").resize((50,50))
        hongoVerde = Image.open("assets/images/hongoVerde.png").resize((40, 40))
        hongoRojo = Image.open("assets/images/hongoRojo.png").resize((40, 40))

        
        self.imgs["inicial"]  = ImageTk.PhotoImage(inicial)
        self.imgs["inicialGrande"]  = ImageTk.PhotoImage(inicialGrande)
        self.imgs["inicialI"] = ImageTk.PhotoImage(base_i)
        self.imgs["izquierda"]= ImageTk.PhotoImage(izq)
        self.imgs["derecha"]  = ImageTk.PhotoImage(der)
        self.imgs["hongoVerde"] = ImageTk.PhotoImage(hongoVerde)
        self.imgs["hongoRojo"] = ImageTk.PhotoImage(hongoRojo)


    def start_game(self):
        # destruyo menú, muestro canvas y creo jugadores
        self.menu.destroy()
        self.canvas.pack(pady=20)

        p1 = Jugador(1, "Jugador1", self.ancho//2, self.alto//2)
        self.add_player(p1, "inicial")
        #Calcular random posicion para el hongo entre 0  y 800
        posicionX = random.randint(0, self.ancho-40)
        self.hongoRojo = self.canvas.create_image(posicionX, self.alto // 2, image=self.imgs["hongoRojo"])

        posicionX = random.randint(0, self.ancho-40)
        self.hongoVerde = self.canvas.create_image(posicionX, self.alto // 2, image=self.imgs["hongoVerde"])

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
        self.check_collisions(p)

    def check_collisions(self, p):
        coords_p = self.canvas.coords(p.canvas_id)
        # Verifico si el personaje colisiona con el hongo verde        
        if hasattr(self, "hongoRojo"):
            coords_h = self.canvas.coords(self.hongoRojo)
            if abs(coords_p[0] - coords_h[0]) < 30 and abs(coords_p[1] - coords_h[1]) < 30:
                self.canvas.delete(self.hongoRojo)
                del self.hongoRojo
                self.crecer_personaje(p)
        if hasattr(self, "hongoVerde"):
            coords_h = self.canvas.coords(self.hongoVerde)
            if abs(coords_p[0] - coords_h[0]) < 30 and abs(coords_p[1] - coords_h[1]) < 30:
                self.canvas.delete(self.hongoVerde)
                del self.hongoVerde
                p.vidas += 1
                self.update_stats(p)

            #self.show_message("¡Comiste hongo de crecimiento!")

        

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

    def crecer_personaje(self, p):
        self.imgs["inicial"]   = self.imgs["inicialGrande"] 
    def run(self):
        self.root.mainloop()
 