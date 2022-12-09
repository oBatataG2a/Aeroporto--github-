class Ticket:
    def __init__(self, ticket=""):
        self.ticket = ticket
        self.tickets = {}

    def addTicket(self, ticket):
        return self.tickets[str(ticket)]

    def verificarTicket(self):
        if self.ticket == self.tickets.values():
            return "Tá limpo"
        else:
            return "Você não é digno"

    def __str__(self):
        return self.verificarTicket()