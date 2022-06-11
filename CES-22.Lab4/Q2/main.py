from pizzacomponent import *

calabresa = Calabresa(Cebola(Base()))
print(calabresa.get_description() + ":$" + str(calabresa.get_totalcost()))

toscana = Calabresa(Cebola(Mussarela(Base())))
print(toscana.get_description() + ":$" + str(toscana.get_totalcost()))

calabacon = Calabresa(Cebola(Catupiry(Bacon(Base()))))
print(calabacon.get_description() + ":$" + str(calabacon.get_totalcost()))

frangocap = Frango(Cebola(Catupiry(Azeitona(Base()))))
print(frangocap.get_description() + ":$" + str(frangocap.get_totalcost()))

italiana = Calabresa(Cebola(Mussarela(Azeitona(Base()))))
print(italiana.get_description() + ":$" + str(italiana.get_totalcost()))


