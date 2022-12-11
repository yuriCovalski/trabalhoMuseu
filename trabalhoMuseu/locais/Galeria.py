from locais.Local import Local

class Galeria:

    def __init__(self,conjunto_artes: tuple, endereco: str, nome: str, conjunto_locais: list = []):
        self.conjunto_artes = conjunto_artes
        self.endereco = endereco
        self.nome = nome
        self.conjunto_locais = []


    def adicionaLocal(self, local: Local):
            self.conjunto_locais.append(local)
            return 'Adicionado com sucesso'
