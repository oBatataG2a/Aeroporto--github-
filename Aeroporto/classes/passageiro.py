from classes.pessoa import Pessoa

class Passageiro(Pessoa):
    def __init__(self, nome="", idade="", passaporte=""):
        super().__init__(nome,idade)
        self.passaporte = passaporte

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Passaporte: {self.passaporte}"