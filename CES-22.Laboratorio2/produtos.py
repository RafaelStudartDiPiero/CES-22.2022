import abc


class Produto:
    __metaclass__ = abc.ABCMeta

    def __init__(self, pvenda, pcompra, t_imposto):
        self.pvenda = pvenda
        self.pcompra = pcompra
        self.t_imposto = t_imposto
        self.taxa = 0
        self.base = 0
        self.imposto = 0

    @abc.abstractmethod
    def adicionar_produto(self):
        pass

    @abc.abstractmethod
    def alterar_produto(self, str1):
        pass

    @abc.abstractmethod
    def remover_produto(self):
        pass

    @abc.abstractmethod
    def exibir_produto(self):
        pass

    def get_imposto(self):
        return self.imposto
