import abc
import compras


class Pessoa:
    __metaclass__ = abc.ABCMeta

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def set_nome(self, name):
        self.name = name

    def get_nome(self):
        return self.name

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email


class Cliente(Pessoa):

    def __init__(self, name, email):
        super().__init__(name, email)
        self.compras = []
        self.quant_comp = 1

    def adicionar_compra(self, dictp):
        new_compra = compras.OrdemCompra(self.quant_comp, dictp)
        self.quant_comp += 1
        self.compras.append(new_compra)

    def busca_compra(self, n):
        for compra in self.compras:
            if compra.idx == n:
                return compra
            elif compra.idx > n:
                break
        print("Ordem de Compra com esse índice não encontrada")
        return None

    def alterar_compra(self, n, dictp):
        compra = self.busca_compra(n)
        if compra is not None:
            compra.set_ordem(dictp)

    def remover_compra(self, n):
        compra = self.busca_compra(n)
        if compra is not None:
            self.compras.remove(compra)

    def consultar_compra(self, n):
        compra = self.busca_compra(n)
        if compra is not None:
            compra.exibir_info()


class Autor(Pessoa):

    def __init__(self, name, email):
        super().__init__(name, email)
        self.titulos = []

    def adicionar_livro(self, livro):
        self.titulos.append(livro)

    def remover_livro(self, livro):
        for liv in self.titulos:
            if liv == livro:
                self.titulos.remove(liv)
                return
        print("Livro não encontrado")

    def mostrar_livro(self):
        for livro in self.titulos:
            livro.exibir_produto()


