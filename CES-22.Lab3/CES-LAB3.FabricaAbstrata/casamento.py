import fabrica
import tipo


class FabricaCasamento(fabrica.FabricaBolo):

    def gerarBoloChoc(self):
        boloChoc = CasamentoChocolate()
        return boloChoc

    def gerarBoloMan(self):
        boloMan = CasamentoMandioca()
        return boloMan

    def gerarBoloCen(self):
        boloCen = CasamentoCenoura()
        return boloCen


class CasamentoChocolate(tipo.Chocolate):
    def __init__(self):
        super().__init__()
        self.estilo = "casamento"


class CasamentoMandioca(tipo.Mandioca):
    def __init__(self):
        super().__init__()
        self.estilo = "casamento"


class CasamentoCenoura(tipo.Cenoura):
    def __init__(self):
        super().__init__()
        self.estilo = "casamento"
