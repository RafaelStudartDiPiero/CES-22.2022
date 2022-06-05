import director
import builder

diretor = director.Diretor()
bolo_builder = builder.BoloBuilder()

diretor.make_bolo(bolo_builder, 'casamento', 'chocolate')
boloCasChoc = bolo_builder.get_result()
boloCasChoc.exibir_info()

diretor.make_bolo(bolo_builder, 'casamento', 'mandioca')
boloCasMan = bolo_builder.get_result()
boloCasMan.exibir_info()

diretor.make_bolo(bolo_builder, 'casamento', 'cenoura')
boloCasCen = bolo_builder.get_result()
boloCasCen.exibir_info()

print('\n')

diretor.make_bolo(bolo_builder, 'informal', 'chocolate')
boloInfChoc = bolo_builder.get_result()
boloInfChoc.exibir_info()

diretor.make_bolo(bolo_builder, 'informal', 'mandioca')
boloInfMan = bolo_builder.get_result()
boloInfMan.exibir_info()

diretor.make_bolo(bolo_builder, 'informal', 'cenoura')
boloInfCen = bolo_builder.get_result()
boloInfCen.exibir_info()

print('\n')

diretor.make_bolo(bolo_builder, 'aniversário', 'chocolate')
boloAnvChoc = bolo_builder.get_result()
boloAnvChoc.exibir_info()

diretor.make_bolo(bolo_builder, 'aniversário', 'mandioca')
boloAnvMan = bolo_builder.get_result()
boloAnvMan.exibir_info()

diretor.make_bolo(bolo_builder, 'aniversário', 'cenoura')
boloAnvCen = bolo_builder.get_result()
boloAnvCen.exibir_info()
