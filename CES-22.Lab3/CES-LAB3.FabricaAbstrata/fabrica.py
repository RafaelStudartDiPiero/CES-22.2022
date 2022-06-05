import abc


class FabricaBolo:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def gerarBoloChoc(self):
        pass

    @abc.abstractmethod
    def gerarBoloMan(self):
        pass

    @abc.abstractmethod
    def gerarBoloCen(self):
        pass
