import datetime

class Funcionamento:
    def __init__(self):
        self.diasFuncionais = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    def verificarFuncionamento(self):
        diaAtual = datetime.datetime.now()
        diaSemana = (diaAtual.strftime("%A"))
        res = [x for x in diaSemana if diaSemana not in self.diasFuncionais]
        if not res:
            return "O Aeroporto está aberto"
        else:
           return "O Aeroporto está fechado"
        
    def __str__(self):
        return self.verificarFuncionamento()