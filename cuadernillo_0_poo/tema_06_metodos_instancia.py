"""Cuadernillo 0 - POO - Tema 6: Metodos de instancia."""

class Ticket:
    def __init__(self, requester: str) -> None:
        self.requester = requester

    def show(self) -> None:
        print(f"Ticket de {self.requester}")


ticket = Ticket("Ana Lopez")
ticket.show()
