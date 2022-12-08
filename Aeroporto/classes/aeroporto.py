class Aeroporto:
    def __init__ (self, nome="", cidade="", estado=""):
        self.nome = nome
        self.cidade = cidade
        self.estado = estado
    
    def __str__(self):
        return f"Nome: {self.nome} Cidade: {self.cidade} Estado: {self.estado}"