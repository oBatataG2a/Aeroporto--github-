import random
from classes.pessoa import Pessoa

class Passageiro(Pessoa):
    def __init__(self, idTicket="", nome="", idade=""):
        super().__init__(nome,idade)
        self.idTicket = idTicket

