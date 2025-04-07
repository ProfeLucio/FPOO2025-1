from vehiculo import Vehiculo

class AutoF1 (Vehiculo):
    def acelerar(self):
        self.velocidad += 40


class Moto (Vehiculo):
    cilindrada: int = 0

class MotoP (Moto):
    def acelerar(self):
        self.velocidad += 5

moto = MotoP()
moto.acelerar()
moto.acelerar()
moto.acelerar()
print(moto.velocidad)