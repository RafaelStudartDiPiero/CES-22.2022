import abc


class User:
    __metaclass__ = abc.ABCMeta

    def __init__(self, name, is_admin):
        self.name = name
        self.is_admin = is_admin
