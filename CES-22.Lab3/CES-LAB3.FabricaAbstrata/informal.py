import fabrica
import tipo


class FabricaInformal(fabrica.FabricaBolo):

    def gerarBoloChoc(self):
        boloChoc = InformalChocolate()
        return boloChoc

    def gerarBoloMan(self):
        boloMan = InformalMandioca()
        return boloMan

    def gerarBoloCen(self):
        boloCen = InformalCenoura()
        return boloCen


class InformalChocolate(tipo.Chocolate):
    def __init__(self):
        super().__init__()
        self.estilo = "informal"


class InformalMandioca(tipo.Mandioca):
    def __init__(self):
        super().__init__()
        self.estilo = "informal"


class InformalCenoura(tipo.Cenoura):
    def __init__(self):
        super().__init__()
        self.estilo = "informal"
