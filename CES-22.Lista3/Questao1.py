import abc


class AbstractPolygon(object):
    """Abstract Class that represents a Square"""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_area(self):
        """Returns area of a polygon"""


class Square(AbstractPolygon):
    """Class that represents a Square"""
    def __init__(self, length):
        self.length = length
        self.sides = 4

    def get_area(self):
        """Returns the area of a square"""
        return self.length * self.length

    def get_perimeter(self):
        """Returns the perimeter of a square"""
        return 4*self.length

    def internal_angle(self):
        """Returns the internal angle of a square"""
        return self.calculate_angle(self.sides)

    @staticmethod
    def calculate_angle(n):
        """Calculates the internal angle of a polygon with n sides"""
        return (180*(n-2))/n

    @classmethod
    def square_information(cls):
        """Prints general information about squares."""
        print('A square is a polygon that has 4 sides with same length.')


# Called a class method , so there isn't a need to instantiate an object
Square.square_information()

# Called a static method, so there isn't a need to instantiate an object.
# A static method can't access class or instance variables or methods.
print(f"Internal Angle by static method:{Square.calculate_angle(4)}")

# Instantiates a Square Object
my_square = Square(8)

# Uses a abstract method that was defined in AbstractPolygon and implemented in Square.
# This way, classes that inherits from AbstractPolygon can have different implementations.
print(f'Area:{my_square.get_area()}')

# Uses a instance method that was defined and implemented in Square Class.
print(f"Perimeter:{my_square.get_perimeter()}")

# Uses a instance method that was defined and implemented in Square Class.
# This method uses a staticmethod as part of its implementation.
print(f"Internal Angle:{my_square.internal_angle()}")

