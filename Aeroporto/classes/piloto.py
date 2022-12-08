from classes.pessoa import Pessoa

class Piloto(Pessoa):
    def __init__ (self, nome="", idade="", rg="", especializacao=""):
        super().__init__(nome, idade)
        self.rg = rg
        self.esp = especializacao
        
    def __str__ (self):
        return f" Nome: {self.nome}, Idade: {self.idade}, RG: {self.rg}, Especialidade: {self.esp}"