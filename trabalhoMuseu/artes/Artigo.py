from artes import IDocumentacao as interface
from alheios import date

class Artigo(interface):

    def __init__(self, ARNI: str, titulo: str, data_publicacao: date, descricao: str):
        self.__arni = ARNI
        self.titulo = titulo
        self.data_publicacao = data_publicacao
        self.descricao = descricao

    @property
    def arni(self):
        return self.__arni

    def anrni(self, arni):
        self.__arni = arni

    def atualizaDocumentacao(self, ARNI = None, titulo = None,
                             data_publicacao = None, descricao = None):
        if ARNI != None:
            self.__arni = ARNI
        if titulo != None:
            self.titulo = titulo
        if data_publicacao != None:
            self.data_publicacao = data_publicacao
        if descricao != None:
            self.descricao = descricao
        return "O novo documento possui agora: " + \
               f"{[self.__arni, self.titulo, self.data_publicacao, self.descricao]}"

    def __str__(self):
        return f"Título: {self.titulo}"

    def __repr__(self):
        return f"{self.titulo}, {self.descricao}, Publicação: {self.data_publicacao}"