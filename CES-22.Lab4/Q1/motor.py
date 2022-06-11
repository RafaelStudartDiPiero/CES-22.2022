class Motor:
    def __init__(self):
        self.potencia = 0

    def get_potencia(self):
        return self.potencia


class MotorEletrico(Motor):
    def __init__(self):
        super().__init__()
        self.potencia = 1


class MotorHibrido(Motor):
    def __init__(self):
        super().__init__()
        self.potencia = 1.5


class MotorCombustao(Motor):
    def __init__(self):
        super().__init__()
        self.potencia = 2
