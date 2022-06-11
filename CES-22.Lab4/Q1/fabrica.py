import motor
import veiculo


class FabricaVeiculo:

    def create_veiculo_eletrico(self):
        newmotor = motor.MotorEletrico()
        return veiculo.Veiculo(newmotor)

    def create_veiculo_hibrido(self):
        newmotor = motor.MotorHibrido()
        return veiculo.Veiculo(newmotor)

    def create_veiculo_combustao(self):
        newmotor = motor.MotorCombustao()
        return veiculo.Veiculo(newmotor)


class FabricaCaminhao:

    def create_veiculo_eletrico(self):
        newmotor = motor.MotorEletrico()
        return veiculo.Caminhao(newmotor)

    def create_veiculo_hibrido(self):
        newmotor = motor.MotorHibrido()
        return veiculo.Caminhao(newmotor)

    def create_veiculo_combustao(self):
        newmotor = motor.MotorCombustao()
        return veiculo.Caminhao(newmotor)


class FabricaCarro:

    def create_veiculo_eletrico(self):
        newmotor = motor.MotorEletrico()
        return veiculo.Carro(newmotor)

    def create_veiculo_hibrido(self):
        newmotor = motor.MotorHibrido()
        return veiculo.Carro(newmotor)

    def create_veiculo_combustao(self):
        newmotor = motor.MotorCombustao()
        return veiculo.Carro(newmotor)


class FabricaMoto:

    def create_veiculo_eletrico(self):
        newmotor = motor.MotorEletrico()
        return veiculo.Moto(newmotor)

    def create_veiculo_hibrido(self):
        newmotor = motor.MotorHibrido()
        return veiculo.Moto(newmotor)

    def create_veiculo_combustao(self):
        newmotor = motor.MotorCombustao()
        return veiculo.Moto(newmotor)
