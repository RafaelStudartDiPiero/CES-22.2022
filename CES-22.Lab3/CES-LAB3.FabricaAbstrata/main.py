import aniversario
import casamento
import informal

Aniv = aniversario.FabricaAniversario()
Cas = casamento.FabricaCasamento()
Inf = informal.FabricaInformal()

AnivChoc = Aniv.gerarBoloChoc()
AnivChoc.mostrar_tipo()
AnivChoc.mostrar_estilo()

print("\n")

AnivMan = Aniv.gerarBoloMan()
AnivMan.mostrar_tipo()
AnivMan.mostrar_estilo()

print("\n")

AnivCen = Aniv.gerarBoloCen()
AnivCen.mostrar_tipo()
AnivCen.mostrar_estilo()

print("\n")

CasChoc = Cas.gerarBoloChoc()
CasChoc.mostrar_tipo()
CasChoc.mostrar_estilo()

print("\n")

CasMan = Cas.gerarBoloMan()
CasMan.mostrar_tipo()
CasMan.mostrar_estilo()

print("\n")

CasCen = Cas.gerarBoloCen()
CasCen.mostrar_tipo()
CasCen.mostrar_estilo()

print("\n")

InfChoc = Inf.gerarBoloChoc()
InfChoc.mostrar_tipo()
InfChoc.mostrar_estilo()

print("\n")

InfMan = Inf.gerarBoloMan()
InfMan.mostrar_tipo()
InfMan.mostrar_estilo()

print("\n")

InfCen = Inf.gerarBoloCen()
InfCen.mostrar_tipo()
InfCen.mostrar_estilo()

print("\n")