import fabrica

fabCaminhao = fabrica.FabricaCaminhao()
fabCarro = fabrica.FabricaCarro()
fabMoto = fabrica.FabricaMoto()
print('')
CamEle = fabCaminhao.create_veiculo_eletrico()
CamEle.acelerar()
CamEle.get_info()
print('')
CamHib = fabCaminhao.create_veiculo_hibrido()
CamHib.acelerar()
CamHib.get_info()
print('')
CamCom = fabCaminhao.create_veiculo_combustao()
CamCom.acelerar()
CamCom.get_info()
print('\n')
CarEle = fabCarro.create_veiculo_eletrico()
CarEle.acelerar()
CarEle.get_info()
print('')
CarHib = fabCarro.create_veiculo_hibrido()
CarHib.acelerar()
CarHib.get_info()
print('')
CarCom = fabCarro.create_veiculo_combustao()
CarCom.acelerar()
CarCom.get_info()
print('\n')
MotEle = fabMoto.create_veiculo_eletrico()
MotEle.acelerar()
MotEle.get_info()
print('')
MotHib = fabMoto.create_veiculo_hibrido()
MotHib.acelerar()
MotHib.get_info()
print('')
MotCom = fabMoto.create_veiculo_combustao()
MotCom.acelerar()
MotCom.get_info()