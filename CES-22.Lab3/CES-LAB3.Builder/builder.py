import abc
import bolo

class Builder:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def reset(self):
        pass

    @abc.abstractmethod
    def set_estilo(self,estilo):
        pass

    @abc.abstractmethod
    def set_tipo(self, tipo):
        pass


class BoloBuilder(Builder):

    def __init__(self):
        self.bolo = None

    def reset(self):
        self.bolo = bolo.Bolo()

    def set_estilo(self,estilo):
        self.bolo.set_estilo(estilo)

    def set_tipo(self, tipo):
        self.bolo.set_tipo(tipo)

    def get_result(self):
        return self.bolo

