import abc


class Comando:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self, cliente=None, valor=0):
        pass


class VerificarSaldo(Comando):
    def execute(self, cliente = None, valor=0):
        return cliente.get_saldo()


class VerificarExtrato(Comando):
    def execute(self, cliente=None, valor=0):
        extrato = cliente.get_extrato()
        return extrato[-3:]


class RealizarDeposito(Comando):
    def execute(self, cliente=None, valor=0):
        saldo_atual = cliente.get_saldo()
        cliente.set_saldo(saldo_atual + int(valor))


class RealizarTransferencia(Comando):
    def execute(self, cliente=None, valor=0):
        saldo_atual = cliente.get_saldo()
        cliente.set_saldo(saldo_atual-int(valor))
