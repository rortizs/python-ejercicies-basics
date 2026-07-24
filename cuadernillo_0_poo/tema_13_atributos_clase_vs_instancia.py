"""Cuadernillo 0 - POO - Tema 13: Atributos de clase vs atributos de instancia."""

class Ticket:
    PRIORIDADES_VALIDAS = {"BAJA", "MEDIA", "ALTA"}  # atributo de clase

    def __init__(self, priority: str) -> None:
        self.priority = priority  # atributo de instancia


print(Ticket.PRIORIDADES_VALIDAS)
ticket = Ticket("ALTA")
print(ticket.priority)
