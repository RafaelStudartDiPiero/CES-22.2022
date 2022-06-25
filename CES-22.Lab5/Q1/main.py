from comando import *
from tkinter import *
from cliente import Cliente


class SisBanco:
    def __init__(self, master=None):
        self.cliente = Cliente()
        self.comandos = []
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 20
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["padx"] = 20
        self.container9["pady"] = 20
        self.container9.pack()

        self.titulo = Label(self.container1, text="* Interface do Banco *")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lbsaldo_part = Label(self.container2, text='Saldo=', font=self.fonte, width=15)
        self.lbsaldo_part.pack(side=LEFT)

        self.txtsaldo_part = Entry(self.container2)
        self.txtsaldo_part["width"] = 10
        self.txtsaldo_part["font"] = self.fonte
        self.txtsaldo_part.pack(side=LEFT)

        self.btnSaldo = Button(self.container2, text="Mostrar Saldo", font=self.fonte, width=10)
        self.btnSaldo["command"] = self.mostrarsaldo
        self.btnSaldo.pack(side=RIGHT)

        self.lbdeposito_part = Label(self.container3, text='Depósito=', font=self.fonte, width=10)
        self.lbdeposito_part.pack(side=LEFT)

        self.txtdeposito_part = Entry(self.container3)
        self.txtdeposito_part["width"] = 25
        self.txtdeposito_part["font"] = self.fonte
        self.txtdeposito_part.pack(side=LEFT)

        self.lbtransferencia_part = Label(self.container4, text='Transfêrencia=', font=self.fonte, width=12)
        self.lbtransferencia_part.pack(side=LEFT)

        self.txttransferencia_part = Entry(self.container4)
        self.txttransferencia_part["width"] = 25
        self.txttransferencia_part["font"] = self.fonte
        self.txttransferencia_part.pack(side=LEFT)

        self.lbsenha_part = Label(self.container5, text='Senha=', font=self.fonte, width=10)
        self.lbsenha_part.pack(side=LEFT)

        self.txtsenha_part = Entry(self.container5)
        self.txtsenha_part["width"] = 25
        self.txtsenha_part["font"] = self.fonte
        self.txtsenha_part.pack(side=LEFT)

        self.bntDepositar = Button(self.container6, text="Depositar", font=self.fonte, width=12)
        self.bntDepositar["command"] = self.depositar
        self.bntDepositar.pack(side=LEFT)

        self.bntTransferir = Button(self.container6, text="Transferir", font=self.fonte, width=12)
        self.bntTransferir["command"] = self.transferir
        self.bntTransferir.pack(side=LEFT)

        self.bntExtrato = Button(self.container6, text="Extrato", font=self.fonte, width=12)
        self.bntExtrato["command"] = self.extrato
        self.bntExtrato.pack(side=LEFT)

        self.lblmsg = Label(self.container7, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

        self.lblextrato = Label(self.container8, text="")
        self.lblextrato["font"] = ("Verdana", "9", "italic")
        self.lblextrato.pack()

        self.lblcomandos = Label(self.container9, text="")
        self.lblcomandos["font"] = ("Verdana", "9", "italic")
        self.lblcomandos.pack()

    def mostrarsaldo(self):
        vsaldo = VerificarSaldo()
        saldo = vsaldo.execute(self.cliente)

        self.lblmsg["text"] = 'Saldo Atualizado'

        self.txtsaldo_part.delete(0, END)
        self.txtsaldo_part.insert(INSERT, saldo)
        self.atualizar_historico('Mostrar Saldo')

    def depositar(self):
        rdeposito = RealizarDeposito()
        deposito = self.txtdeposito_part.get()
        if deposito == '':
            deposito = 0

        self.lblmsg["text"] = 'Depósito Realizado'

        rdeposito.execute(self.cliente, deposito)
        self.txtdeposito_part.delete(0, END)
        self.atualizar_historico('Depósito')

    def transferir(self):
        rtransferencia = RealizarTransferencia()
        transferencia = self.txttransferencia_part.get()
        if transferencia == '':
            transferencia = 0

        self.lblmsg["text"] = 'Transferência Realizada'

        rtransferencia.execute(self.cliente, transferencia)
        self.txttransferencia_part.delete(0, END)
        self.atualizar_historico('Transferência')

    def extrato(self):
        vextrato = VerificarExtrato()
        extrato = vextrato.execute(self.cliente)

        string = 'Últimas Operações:'
        for i in extrato:
            t = str(i)
            if i > 0:
                t = '+' + str(i)
            string = string + t + ','
        self.lblmsg["text"] = 'Extrato Atualizado'
        self.lblextrato["text"] = string
        self.atualizar_historico('Obter Extrato')

    def atualizar_historico(self, string):
        if len(self.comandos) >= 4:
            self.comandos.pop(0)
        self.comandos.append(string)
        label = 'Histórico:'
        for i in self.comandos:
            label = label + i + ','
        self.lblcomandos["text"] = label


root = Tk()
SisBanco(root)
root.mainloop()
