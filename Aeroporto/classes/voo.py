class Voo:
    def __init__(self, name="", valor="", assentos=0):
        self.name = name
        self.valor = valor
        self.ass = assentos

    def getStatus(self):
        return f" O voo {self.name}\n Possui {self.ass} assentos disponiveis"

    def precoInfo(self):
        return f"O preço por ticket é de: {self.valor}"

    def reservarTicket(self):
        if (self.ass>0):
            return f"O seu ticket foi reservado! O número do seu assento é o: {self.ass}", self.ass -1
        else:
            return f"Tá lotado, piá"

    def __str__(self):
        return f"{self.getStatus()}\n {self.reservarTicket()}\n {self.precoInfo()}"