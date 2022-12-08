class Aviao:
    def __init__ (self, cargaMax="", modelo=""):   
        self.cargaMax = cargaMax
        self.modelo = modelo
    
    def __str__(self):
        return f" Carga Máxima: {self.cargaMax} Modelo: {self.modelo}"
