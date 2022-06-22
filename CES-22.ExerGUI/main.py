from participantes import Participante
from tkinter import *

class SisPart:
    def __init__(self, master= None):
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
        self.container8["pady"] = 5
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["padx"] = 20
        self.container9["pady"] = 5
        self.container9.pack()
        self.container10 = Frame(master)
        self.container10["padx"] = 20
        self.container10["pady"] = 5
        self.container10.pack()
        self.container11 = Frame(master)
        self.container11["padx"] = 20
        self.container11["pady"] = 10
        self.container11.pack()
        self.container12 = Frame(master)
        self.container12["pady"] = 15
        self.container12.pack()

        self.titulo = Label(self.container1, text="* Registro de Participantes *")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lbid_part = Label(self.container2, text='Id=', font=self.fonte, width=15)
        self.lbid_part.pack(side=LEFT)

        self.txtid_part = Entry(self.container2)
        self.txtid_part["width"] = 10
        self.txtid_part["font"] = self.fonte
        self.txtid_part.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarParti
        self.btnBuscar.pack(side=RIGHT)

        self.lbnome_part = Label(self.container3, text='Nome=', font=self.fonte, width=10)
        self.lbnome_part.pack(side=LEFT)

        self.txtnome_part = Entry(self.container3)
        self.txtnome_part["width"] = 25
        self.txtnome_part["font"] = self.fonte
        self.txtnome_part.pack(side=LEFT)

        self.lblogin_part = Label(self.container4, text='Login=', font=self.fonte, width=10)
        self.lblogin_part.pack(side=LEFT)

        self.txtlogin_part = Entry(self.container4)
        self.txtlogin_part["width"] = 25
        self.txtlogin_part["font"] = self.fonte
        self.txtlogin_part.pack(side=LEFT)

        self.lbsenha_part = Label(self.container5, text='Senha=', font=self.fonte, width=10)
        self.lbsenha_part.pack(side=LEFT)

        self.txtsenha_part = Entry(self.container5)
        self.txtsenha_part["width"] = 25
        self.txtsenha_part["font"] = self.fonte
        self.txtsenha_part.pack(side=LEFT)

        self.lbemail_part = Label(self.container6, text='Email=', font=self.fonte, width=10)
        self.lbemail_part.pack(side=LEFT)

        self.txtemail_part = Entry(self.container6)
        self.txtemail_part["width"] = 25
        self.txtemail_part["font"] = self.fonte
        self.txtemail_part.pack(side=LEFT)

        self.lbendereco_part = Label(self.container7, text='Endereço=', font=self.fonte, width=10)
        self.lbendereco_part.pack(side=LEFT)

        self.txtendereco_part = Entry(self.container7)
        self.txtendereco_part["width"] = 25
        self.txtendereco_part["font"] = self.fonte
        self.txtendereco_part.pack(side=LEFT)

        self.lbtelefone_part = Label(self.container8, text='Telefone=', font=self.fonte, width=10)
        self.lbtelefone_part.pack(side=LEFT)

        self.txttelefone_part = Entry(self.container8)
        self.txttelefone_part["width"] = 25
        self.txttelefone_part["font"] = self.fonte
        self.txttelefone_part.pack(side=LEFT)

        self.bntInsert = Button(self.container9, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirParti
        self.bntInsert.pack(side=LEFT)

        self.bntAlterar = Button(self.container9, text="Alterar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarParti
        self.bntAlterar.pack(side=LEFT)

        self.bntExcluir = Button(self.container9, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirParti
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container10, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

    def inserirParti(self):
        parti = Participante()
        parti.nome = self.txtnome_part.get()
        parti.login = self.txtlogin_part.get()
        parti.senha = self.txtsenha_part.get()
        parti.email = self.txtemail_part.get()
        parti.endereco = self.txtendereco_part.get()
        parti.telefone = self.txttelefone_part.get()

        self.lblmsg["text"] = parti.insertParticipante()

        self.txtid_part.delete(0, END)
        self.txtnome_part.delete(0, END)
        self.txtlogin_part.delete(0, END)
        self.txtsenha_part.delete(0, END)
        self.txtemail_part.delete(0, END)
        self.txtendereco_part.delete(0, END)
        self.txttelefone_part.delete(0, END)

    def alterarParti(self):
        parti = Participante()
        parti.id = self.txtid_part.get()
        parti.nome = self.txtnome_part.get()
        parti.login = self.txtlogin_part.get()
        parti.senha = self.txtsenha_part.get()
        parti.email = self.txtemail_part.get()
        parti.endereco = self.txtendereco_part.get()
        parti.telefone = self.txttelefone_part.get()

        self.lblmsg["text"] = parti.alterarParticipante

        self.txtid_part.delete(0, END)
        self.txtnome_part.delete(0, END)
        self.txtlogin_part.delete(0, END)
        self.txtsenha_part.delete(0, END)
        self.txtemail_part.delete(0, END)
        self.txtendereco_part.delete(0, END)
        self.txttelefone_part.delete(0, END)

    def excluirParti(self):
        parti = Participante()
        parti.id = self.txtid_part.get()

        self.lblmsg["text"] = parti.deletarParticipante

        self.txtid_part.delete(0, END)
        self.txtnome_part.delete(0, END)
        self.txtlogin_part.delete(0, END)
        self.txtsenha_part.delete(0, END)
        self.txtemail_part.delete(0, END)
        self.txtendereco_part.delete(0, END)
        self.txttelefone_part.delete(0, END)

    def buscarParti(self):
        parti = Participante()
        id = self.txtid_part.get()

        self.lblmsg["text"] = parti.buscarParticipante(id)

        self.txtid_part.delete(0, END)
        self.txtid_part.insert(INSERT, parti.id)
        self.txtnome_part.delete(0, END)
        self.txtnome_part.insert(INSERT, parti.nome)
        self.txtlogin_part.delete(0, END)
        self.txtlogin_part.insert(INSERT, parti.login)
        self.txtsenha_part.delete(0, END)
        self.txtsenha_part.insert(INSERT, parti.senha)
        self.txtemail_part.delete(0, END)
        self.txtemail_part.insert(INSERT, parti.email)
        self.txtendereco_part.delete(0, END)
        self.txtendereco_part.insert(INSERT, parti.endereco)
        self.txttelefone_part.delete(0, END)
        self.txttelefone_part.insert(INSERT, parti.telefone)


root = Tk()
SisPart(root)
root.mainloop()