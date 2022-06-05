import fabrica
import tipo


class FabricaAniversario(fabrica.FabricaBolo):

    def gerarBoloChoc(self):
        boloChoc = AniversarioChocolate()
        return boloChoc

    def gerarBoloMan(self):
        boloMan = AniversarioMandioca()
        return boloMan

    def gerarBoloCen(self):
        boloCen = AniversarioCenoura()
        return boloCen


class AniversarioChocolate(tipo.Chocolate):
    def __init__(self):
        super().__init__()
        self.estilo = "aniversário"


class AniversarioMandioca(tipo.Mandioca):
    def __init__(self):
        super().__init__()
        self.estilo = "aniversário"


class AniversarioCenoura(tipo.Cenoura):
    def __init__(self):
        super().__init__()
        self.estilo = "aniversário"
