class OrdemCompra:
    def __init__(self, idx, dictp):
        self.idx = idx
        self.ordem = dictp

    def exibir_info(self):
        for key, value in self.ordem.items():
            print('Qtd:', value)
            key.exibir_produto()

    def set_ordem(self, dictp):
        self.ordem = dictp
