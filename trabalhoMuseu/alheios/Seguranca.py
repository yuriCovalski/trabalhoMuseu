from alheios import date,randrange

class Seguranca:

    def __init__(self, n_guardas: int):
        self.n_guardas = n_guardas
        self.guarnicao = []
        self.custo = randrange(1793, 1793*10)

    def rota(self, data_inicio: date, data_fim: date, trajetoria: list):
        return f"NICE! data começo:{data_inicio}, data fim: {data_fim}, {trajetoria}"