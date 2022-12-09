class Carga:
    def __init__(self, qtdCarga=0):
        self.qtdCarga = qtdCarga
    
    def levarCarga(self):
        if self.qtdCarga != 0:
            return f"O avião levará {self.qtdCarga} cargas"
        else:
            return "O avião não levará cargas"

    def __str__(self):
        return self.levarCarga()