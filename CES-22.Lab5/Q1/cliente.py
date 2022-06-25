class Cliente:
    def __init__(self):
        self.saldo = 0
        self.extrato = []

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, saldo):
        dif = -(self.saldo-saldo)
        self.add_extrato(dif)
        self.saldo = saldo

    def get_extrato(self):
        return self.extrato

    def add_extrato(self, op):
        self.extrato.append(op)
