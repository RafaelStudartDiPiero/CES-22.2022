class Bolo:

    def __init__(self):
        self.tipo = "sem Tipo"
        self.estilo = "sem Estilo"

    def set_tipo(self, tipo):
        self.tipo = tipo

    def set_estilo(self, estilo):
         self.estilo = estilo

    def exibir_info(self):
        print('Tenho de estilo :', self.estilo, '\n Sou de : ', self.tipo)
