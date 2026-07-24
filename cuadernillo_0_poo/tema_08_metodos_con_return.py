"""Cuadernillo 0 - POO - Tema 8: Metodos que devuelven un valor."""

class Ticket:
    def __init__(self, priority: str) -> None:
        self.priority = priority

    def es_urgente(self) -> bool:
        return self.priority == "ALTA"


ticket = Ticket("ALTA")
if ticket.es_urgente():
    print("Atender de inmediato")
