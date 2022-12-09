class TorreControle:
    def __init__(self, vooPermitido=True, sim=""):
        self.vooPermitido = vooPermitido
        self.sim = sim

    def verificarCondicoes(self):
        if self.vooPermitido == True:
            return "O voo vai proceder"
        else:
            return "O voo foi cancelado"
    
    def __str__(self):
        return self.verificarCondicoes()