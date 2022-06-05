class Bolo:

    def __init__(self):
        self.tipo = "sem Tipo"
        self.estilo = "sem Estilo"

    def mostrar_tipo(self):
        print("Sou de ", self.tipo)

    def mostrar_estilo(self):
        print("Tenho estilo de ", self.estilo)

class Chocolate(Bolo):
    def __init__(self):
        super().__init__()
        self.tipo = "chocolate"


class Mandioca(Bolo):
    def __init__(self):
        super().__init__()
        self.tipo = "mandioca"


class Cenoura(Bolo):
    def __init__(self):
        super().__init__()
        self.tipo = "cenoura"

