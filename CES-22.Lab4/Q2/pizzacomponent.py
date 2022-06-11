class PizzaComponent:
    def get_description(self):
        return self.__class__.__name__

    def get_totalcost(self):
        return self.__class__.cost


class Base(PizzaComponent):
    cost = 0.0


class Decorator(PizzaComponent):
    def __init__(self, pizzaComponent):
        self.component = pizzaComponent

    def get_description(self):
        return self.component.get_description() + ' ' + PizzaComponent.get_description(self)

    def get_totalcost(self):
        return self.component.get_totalcost() + PizzaComponent.get_totalcost(self)


class Mussarela(Decorator):
    cost = 0.0

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Calabresa(Decorator):
    cost = 5.0

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Catupiry(Decorator):
    cost = 3.0

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Cebola(Decorator):
    cost = 2.0

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Frango(Decorator):
    cost = 4.0

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Azeitona(Decorator):
    cost = 2.0

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Bacon(Decorator):
    cost = 2.0

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)

