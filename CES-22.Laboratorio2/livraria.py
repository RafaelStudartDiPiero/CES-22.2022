import pessoas


class Livraria:

    def __init__(self):
        self.estoque = []
        self.clientes = []
        self.autores = []

    def buscar_cliente(self, cliente):
        for cl in self.clientes:
            if cl.get_nome() == cliente:
                return cl
        return None

    def adicionar_cliente(self, str1, str2):
        newclient = pessoas.Cliente(str1, str2)
        self.clientes.append(newclient)
        return newclient

    def alterar_cliente(self, str1, str2):
        for cliente in self.clientes:
            if cliente.get_nome() == str1:
                cliente.set_email(str2)
                print("Alterado com sucesso.")
                return
        print("Cliente não encontrado")
        return

    def consultar_cliente(self, str1):
        for cliente in self.clientes:
            if cliente.get_nome() == str1:
                print("Dados:")
                print("Nome:", cliente.get_nome())
                print("Email:", cliente.get_email())
                return
        print("Cliente não encontrado")
        return

    def remover_cliente(self, str1):
        for cliente in self.clientes:
            if cliente.get_nome() == str1:
                self.clientes.remove(cliente)
                print("Removido com sucesso")
                return
        print("Cliente não encontrado")
        return

    def adicionar_produto(self, produto):
        self.estoque.append(produto)
        produto.adicionar_produto()

    def alterar_produto(self, produto, str1):
        for prod in self.estoque:
            if prod == produto:
                prod.alterar_produto(str1)
                return
        print("Produto não encontrado")
        return

    def remover_produto(self, produto):
        for prod in self.estoque:
            if prod == produto:
                prod.remover_produto()
                self.estoque.remove(prod)
                return
        print("Produto não encontrado")
        return

    def consultar_produto(self, produto):
        for prod in self.estoque:
            if prod == produto:
                prod.exibir_produto()
                return
        print("Produto não encontrado")
        return

    def adicionar_ordemcompra(self, cliente, dictp):
        cl = self.buscar_cliente(cliente)
        if cl is not None:
            cl.adicionar_compra(dictp)

    def remover_ordemcompra(self, cliente, idx):
        cl = self.buscar_cliente(cliente)
        if cl is not None:
            cl.remover_compra(idx)

    def alterar_ordemcompra(self, cliente, dictp, idx):
        cl = self.buscar_cliente(cliente)
        if cl is not None:
            cl.alterar_compra(idx, dictp)

    def consultar_ordemcompra(self, cliente, idx):
        cl = self.buscar_cliente(cliente)
        if cl is not None:
            cl.consultar_compra(idx)

    def adicionar_autor(self, str1, str2):
        newautor = pessoas.Autor(str1, str2)
        self.autores.append(newautor)
        return newautor

    def remover_autor(self, str1):
        for autor in self.autores:
            if autor.get_nome() == str1:
                self.autores.remove(autor)
                return
        print("Autor não encontrado")
        return
