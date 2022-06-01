import produtos


class Livro(produtos.Produto):

    def __init__(self, pvenda, pcompra, t_imposto, titulo, autor, edicao, editora, genero):
        super().__init__(pvenda, pcompra, t_imposto)
        self.titulo = titulo
        self.autor = autor
        self.edicao = edicao
        self.editora = editora
        self.genero = genero
        self.taxa, self.base = self.genero.calc_impostos()
        self.imposto = self.t_imposto.imposto_func(self.pvenda, self.pcompra, self.taxa, self.base)

    def adicionar_produto(self):
        self.autor.adicionar_livro(self)

    def alterar_produto(self, str1):
        self.titulo = str1

    def remover_produto(self):
        self.autor.remover_livro(self)

    def exibir_produto(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor.get_nome())
        print("Edição:", self.edicao)
        print("Editora:", self.editora)
        print("Gênero:", self.genero.nome)
        print("Preço de Venda:", self.pvenda)
        print("Preço de Compra:", self.pcompra)
        print("Imposto:", self.get_imposto())
        print("\n")
        return

    def get_imposto(self):
        self.imposto = self.t_imposto.imposto_func(self.pvenda, self.pcompra, self.taxa, self.base)
        return self.imposto