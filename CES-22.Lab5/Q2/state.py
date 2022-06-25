import abc


class State:
    __metaclass__ = abc.ABCMeta

    def __init__(self, document):
        self.document = document
        self.name = None

    def render(self, user):
        is_author = (user == self.document.author)
        if user.is_admin or is_author:
            print('Título:', self.document.title)
            print('Autor:', self.document.author.name)
            print('Estado:', self.name)
        else:
            print('Acesso Negado')


    @abc.abstractmethod
    def publish(self, user):
        pass

    @abc.abstractmethod
    def go_back(self, user):
        pass


class Draft(State):
    def __init__(self, document):
        super().__init__(document)
        self.name = 'Rascunho'

    def publish(self, user):
        if user.is_admin:
            self.document.change_state(Published(self.document))
        else:
            self.document.change_state(Moderation(self.document))

    def go_back(self, user):
        print('Operação não existe')


class Moderation(State):
    def __init__(self, document):
        super().__init__(document)
        self.name = 'Moderação'

    def publish(self, user):
        if user.is_admin:
            self.document.change_state(Published(self.document))
        else:
            print('Acesso Negado')

    def go_back(self, user):
        if user.is_admin:
            self.document.change_state(Draft(self.document))
        else:
            print('Acesso Negado')


class Published(State):
    def __init__(self, document):
        super().__init__(document)
        self.name = 'Publicado'

    def publish(self, user):
        print('Operação não existe')

    def go_back(self, user):
        if user.is_admin:
            self.document.change_state(Draft(self.document))
        else:
            print('Acesso Negado')
