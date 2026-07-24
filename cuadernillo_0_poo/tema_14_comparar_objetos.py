"""Cuadernillo 0 - POO - Tema 14: Comparar dos objetos por sus atributos."""

class Ticket:
    def __init__(self, requester: str) -> None:
        self.requester = requester

    def mismo_solicitante(self, otro: "Ticket") -> bool:
        return self.requester == otro.requester


ticket_a = Ticket("Ana Lopez")
ticket_b = Ticket("Ana Lopez")
print(ticket_a.mismo_solicitante(ticket_b))  # True
