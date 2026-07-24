"""Cuadernillo 0 - POO - Tema 10: Encapsulamiento por convencion (atributos protegidos)."""

class Ticket:
    def __init__(self) -> None:
        self._estado = "ABIERTO"

    def obtener_estado(self) -> str:
        return self._estado


ticket = Ticket()
print(ticket.obtener_estado())
