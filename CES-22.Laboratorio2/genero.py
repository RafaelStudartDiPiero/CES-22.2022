import abc


class Genero:
    __metaclass__ = abc.ABCMeta

    def __init__(self, nome):
        self.nome = nome
        self.taxa = 0
        self.base = 0

    def calc_impostos(self):
        return self.taxa, self.base


class Suspense(Genero):
    def __init__(self, nome):
        super().__init__(nome)
        self.taxa = 3
        self.base = 1


class Juvenil(Genero):
    def __init__(self, nome):
        super().__init__(nome)
        self.taxa = 1
        self.base = 0.5


class Romance(Genero):
    def __init__(self, nome):
        super().__init__(nome)
        self.taxa = 2
        self.base = 1
