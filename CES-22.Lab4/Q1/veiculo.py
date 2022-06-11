class Veiculo:

    def __init__(self, motor):
        self.velocidade = 10
        self.motor = motor
        self.taxa = 0

    def acelerar(self):
        self.velocidade += self.taxa * self.motor.get_potencia()

    def get_info(self):
        print('Sou um Veículo, com velocidade:', self.velocidade)
        print('Tenho um motor:', self.motor.__class__.__name__)


class Caminhao(Veiculo):
    def __init__(self, motor):
        super().__init__(motor)
        self.taxa = 0.5

    def get_info(self):
        print('Sou um Caminhão, com velocidade:', self.velocidade)
        print('Tenho um motor:', self.motor.__class__.__name__)


class Carro(Veiculo):
    def __init__(self, motor):
        super().__init__(motor)
        self.taxa = 1

    def get_info(self):
        print('Sou um Carro, com velocidade:', self.velocidade)
        print('Tenho um motor:', self.motor.__class__.__name__)


class Moto(Veiculo):
    def __init__(self, motor):
        super().__init__(motor)
        self.taxa = 2

    def get_info(self):
        print('Sou uma Moto, com velocidade:', self.velocidade)
        print('Tenho um motor:', self.motor.__class__.__name__)