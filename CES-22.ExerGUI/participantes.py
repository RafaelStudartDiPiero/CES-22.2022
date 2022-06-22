from banco import Banco


class Participante(object):

    def __init__(self, id=0, nome="", login="", senha="", email="", endereco="", telefone=""):
        self.info = {}
        self.id = id
        self.nome = nome
        self.login = login
        self.senha = senha
        self.email = email
        self.endereco = endereco
        self.telefone = telefone

    def insertParticipante(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute("insert into participantes (nome, login, senha, email, endereco, telefone) values('"+self.nome+"','" +
                      self.login+"','" + self.senha+"','"+self.email+"','"+self.endereco+"','"+self.telefone+"')")

            banco.conexao.commit()
            c.close()
            return "Participante Cadastrado com Sucesso"
        except:
            return "Ocorreu um erro no cadastro"

    @property
    def alterarParticipante(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("update participantes set nome = '" + self.nome + "', login = '" + self.login + "', senha ='" + self.senha +
                      "', email = '" + self.email + "', endereco = '" + self.endereco + "', telefone = '" + self.telefone +
                      "' where id = " + str(self.id) + " ")
            banco.conexao.commit()
            c.close()
            return "Participante Alterado com Sucesso"
        except:
            return "Ocorreu um erro na alteração"

    @property
    def deletarParticipante(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("delete from participantes where id = '" + str(self.id) + "' ")
            banco.conexao.commit()
            c.close()
            return "Participante Deletado com Sucesso"
        except:
            return "Ocorreu um erro na deleção"

    def buscarParticipante(self, id):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("select * from participantes where id = " + id + " ")
            for linha in c:
                self.id = linha[0]
                self.nome = linha[1]
                self.login = linha[2]
                self.senha = linha[3]
                self.email = linha[4]
                self.endereco = linha[5]
                self.telefone = linha[6]
            c.close()
            return "Busca Realizada com Sucesso"
        except:
            return "Ocorreu um erro na busca"