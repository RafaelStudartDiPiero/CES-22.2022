def add_intro(func):
    """Decorator that adds an intro header"""
    def func_wrapper(*args, **kwargs):
        return "Intro Header\n{0}".format(func(*args, **kwargs))
    return func_wrapper


class Person(object):
    """Class that represents a person"""
    def __init__(self, name):
        self.name = name

    @add_intro
    def get_family(self, *args, **kwargs):
        """Informs full name(passed by args) and relatives names(contained in kwargs)"""
        data = self.name
        for arg in args:
            data = data + " " + arg
        data = data + "\nRelatives: \n"
        for kw in kwargs:
            data = data + kw + ':' + kwargs[kw] + '\n'
        return data


person = Person('Rafael')

print(person.get_family('Studart', 'Mattos', 'Di Piero', Father=' Paulo',
                        Mother=' Michele', Brother=' Diego'))
