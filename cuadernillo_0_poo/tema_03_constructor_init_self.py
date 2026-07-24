"""Cuadernillo 0 - POO - Tema 3: El constructor __init__ y el parametro self."""

class Ticket:
    def __init__(self, descripcion: str) -> None:
        self.descripcion = descripcion


ticket = Ticket("No enciende la impresora")
print(ticket.descripcion)
