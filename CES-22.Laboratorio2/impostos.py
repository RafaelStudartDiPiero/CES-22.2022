import abc


class Imposto:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    @abc.abstractmethod
    def imposto_func(self, pvenda, pcompra, taxa, base):
        pass


class BR(Imposto):

    def __init__(self):
        super().__init__()

    def imposto_func(self, pvenda, pcompra, taxa, base):
        imposto = (pvenda + pcompra)*taxa + base
        return imposto


class US(Imposto):

    def __init__(self):
        super().__init__()

    def imposto_func(self, pvenda, pcompra, taxa, base):
        imposto = (pvenda - pcompra) * taxa + base
        return imposto
