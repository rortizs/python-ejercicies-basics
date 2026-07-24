"""Cuadernillo 0 - POO - Tema 12: Representar el objeto como texto: __str__."""

class Ticket:
    def __init__(self, requester: str) -> None:
        self.requester = requester

    def __str__(self) -> str:
        return f"Ticket de {self.requester}"


ticket = Ticket("Ana Lopez")
print(ticket)  # usa __str__ automaticamente
