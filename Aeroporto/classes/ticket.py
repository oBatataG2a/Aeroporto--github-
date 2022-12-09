"""
    Usei o exemplo do site:
    https://www.digitalocean.com/community/tutorials/how-to-compare-two-lists-in-python
    para verificar se o código do ticket está na lista de tickets armazenados
"""

class Ticket:
    def __init__(self, ticket=""):
        self.ticket = ticket
        self.tickets = ["123456","412765","967512"]

    def verificarTicket(self):
        res = [x for x in self.ticket if self.ticket not in self.tickets]
        if not res:
            return "O Ticket é válido"
        else:
           return "O ticket é inválido"

    def __str__(self):
        return self.verificarTicket()