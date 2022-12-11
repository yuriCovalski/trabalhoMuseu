from artes import IDocumentacao as interface
from alheios import date

class Artefatos(interface):

    def __init__(self, AORNI: str, titulo: str, data_recebimento: date, descricao: str):
        self.__aorni = AORNI
        self.titulo = titulo
        self.data_recebimento = data_recebimento
        self.descricao = descricao

    @property
    def aorni(self):
        return self.__aorni

    def aorni(self, aorni):
        self.__aorni = aorni

    def atualizaDocumentacao(self, AORNI = None, titulo = None,
                             data_recebimento = None, descricao = None):
        if AORNI != None:
            self.aorni = AORNI
        if titulo != None:
            self.titulo = titulo
        if data_recebimento != None:
            self.data_recebimento = data_recebimento
        if descricao != None:
            self.descricao = descricao
        return "O novo documento possui agora: " + \
               f"{[self.__aorni, self.titulo, self.data_recebimento, self.descricao]}"

    def __str__(self):
        return f"{self.titulo}"

    def __repr__(self):
        return f"{self.titulo}, {self.descricao}, Publicação: {self.data_recebimento}"

