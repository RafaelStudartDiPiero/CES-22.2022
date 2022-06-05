class Diretor:
    def make_bolo(self, builder, estilo, tipo):
        builder.reset()
        builder.set_estilo(estilo)
        builder.set_tipo(tipo)
