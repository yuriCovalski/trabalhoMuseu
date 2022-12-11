from abc import ABCMeta, abstractstaticmethod


class IDocumentacao(metaclass=ABCMeta):

    @abstractstaticmethod
    def atualizaDocumentacao():
        """ Método de interface """
