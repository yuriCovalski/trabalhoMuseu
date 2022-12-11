import admin.Eventos
import locais.Local
from artes.Artigo import Artigo
from artes.Artefatos import Artefatos

class Artista:

    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.__cpf = cpf
        self.lista_artes = []


    @property
    def cpf(self):
        return self.__cpf

    def cpf(self, cpf):
        self.__cpf = cpf

    def publica_arte(self, arte):
        if type(arte) == Artigo or type(arte) == Artefatos:
            self.lista_artes.append(arte)
            return "Adicionado com sucesso"
        else:
            raise ValueError('arte precisa ser do tipo artigo ou artefatos')

    def faz_evento(self,nome, data, hora,local):
        evento = admin.Eventos.Evento(nome,data,hora,local)
        return f'Evento feito com sucesso, data: {evento.data} ás {evento.hora}.'

    def __str__(self):
        return f"{self.titulo}"
