class Object:
    """Class that represents an object"""
    def __init__(self, name):
        print('Initializing an Object')
        self.label = 'I am an Object'
        self.name = name


class Telephone(Object):
    """Class that represents a telephone"""
    def __init__(self, name):
        print('Initializing a Telephone')
        super().__init__(name)
        self.label = 'I am a Telephone'

    def call(self):
        """Makes a call"""
        print(f'{self.name} is calling')


class Computer(Object):
    """Class that represents a computer"""
    def __init__(self, name):
        print('Initializing a Computer')
        super().__init__(name)
        self.label = 'I am a Computer'

    def calculate(self, n1, n2):
        """Returns the sum of n1 and n2"""
        return n1+n2


class Cellphone(Telephone, Computer):
    """Class that represents a Cellphone"""

    def __init__(self, name):
        print('Initializing a Cellphone')
        # self.label = 'I am a Cellphone'
        super().__init__(name)
        self.label = 'I am a Cellphone'


# This instantiates an Cellphone object, calling it's __init__ function.
# We can observe the order that super() is used by analyzing the printed result.
phone = Cellphone('MyCellPhone')
# Called a method that was inherited from Telephone.
phone.call()
# Called a method that was inherited from Computer.
print(phone.calculate(2, 10))
# If the position of self.label is changed in Cellphone.__init__, this result will change.
print(phone.label)
