import livraria
import genero
import impostos
import livros

Lib = livraria.Livraria()

Edgar = Lib.adicionar_autor("Edgar", "edgar@hotmail.com")
Rick = Lib.adicionar_autor("Rick Riordan", "rick@hotmail.com")

Romance = genero.Romance("Romance")
Suspense = genero.Suspense("Suspense")
Juvenil = genero.Juvenil("Juvenil")

BR = impostos.BR()
US = impostos.US()

Percy = livros.Livro(2, 1, BR, "Percy Jackson", Rick, 1, "EditoraRiordan", Juvenil)
Apollo = livros.Livro(2, 1, US, "Maldição de Apollo", Rick, 2, "EditoraRiordan", Juvenil)
Corvo = livros.Livro(2, 1, BR, "O Corvo", Edgar, 3, "EditoraPoe", Suspense)

Lib.adicionar_produto(Percy)
for produto in Lib.estoque:
    if produto is not None:
        produto.exibir_produto()

Lib.alterar_produto(Percy, "Percy Jackson e os Olimpianos")

for produto in Lib.estoque:
    produto.exibir_produto()

Lib.consultar_produto(Percy)
Lib.consultar_produto(Apollo)

Lib.adicionar_produto(Apollo)

Lib.consultar_produto(Apollo)

# Lib.remover_produto(Apollo)

Lib.consultar_produto(Apollo)

for produto in Lib.estoque:
    produto.exibir_produto()

Lib.adicionar_cliente("Rafael", "rafael@hotmail.com")

for cliente in Lib.clientes:
    print(cliente.get_nome(), cliente.get_email())
print("\n")
Lib.alterar_cliente("Rafael", "rafael@gmail.com")

for cliente in Lib.clientes:                      
    print(cliente.get_nome(), cliente.get_email())
print("\n")

Lib.consultar_cliente("Rafael")
print("\n")
Lib.consultar_cliente("Bruno")
print("\n")

Lib.consultar_cliente("Rafael")
print("\n")


ordemCompra = {
    Percy: 1,
    Apollo: 2,
}

Lib.adicionar_ordemcompra("Rafael", ordemCompra)
for cliente in Lib.clientes:
    for compra in cliente.compras:
        compra.exibir_info()
print("\n")


ordemCompra2 = {
    Percy: 3,
    Apollo: 1,
}
Lib.alterar_ordemcompra("Rafael", ordemCompra2, 1)
for cliente in Lib.clientes:
    for compra in cliente.compras:
        compra.exibir_info()
print("\n")

Lib.consultar_ordemcompra("Rafael", 1)
Lib.remover_ordemcompra("Rafael", 1)
Lib.consultar_ordemcompra("Rafael", 1)
