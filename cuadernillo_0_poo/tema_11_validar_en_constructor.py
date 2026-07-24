"""Cuadernillo 0 - POO - Tema 11: Validar datos dentro del constructor."""

class Ticket:
    PRIORIDADES_VALIDAS = {"BAJA", "MEDIA", "ALTA"}

    def __init__(self, priority: str) -> None:
        priority = priority.strip().upper()
        if priority not in self.PRIORIDADES_VALIDAS:
            raise ValueError("Prioridad no valida")
        self.priority = priority


ticket = Ticket("alta")
print(ticket.priority)
