"""Cuadernillo 0 - POO - Tema 4: Atributos de instancia."""

class Ticket:
    def __init__(self, requester: str, priority: str) -> None:
        self.requester = requester
        self.priority = priority


ticket = Ticket("Ana Lopez", "ALTA")
print(f"{ticket.requester} - {ticket.priority}")
