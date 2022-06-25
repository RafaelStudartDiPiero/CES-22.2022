from state import *


class Document:
    def __init__(self, user, title):
        self.state = Draft(self)
        self.author = user
        self.title = title

    def render(self, user):
        self.state.render(user)

    def publish(self, user):
        self.state.publish(user)

    def go_back(self, user):
        self.state.go_back(user)

    def change_state(self, state):
        self.state = state