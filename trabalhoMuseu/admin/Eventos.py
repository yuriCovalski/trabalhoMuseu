from locais.Local import Local
from alheios import date, time
from alheios.Plateia import Plateia

class Evento:
    def __init__(self, nome: str, data: date, hora: time, local: Local):
        self.nome = nome
        self.data = data
        self.hora = hora
        self.local = local


    def numeroPlateia(self, plateia: Plateia):
        return plateia.n_pessoas