"""Cuadernillo II - Ejercicio 3: Clase Ticket con validación en el constructor."""

class Ticket:
    PRIORIDADES_VALIDAS = {"BAJA", "MEDIA", "ALTA"}

    def __init__(self, ticket_id: int, solicitante: str, prioridad: str) -> None:
        prioridad = prioridad.strip().upper()
        if prioridad not in self.PRIORIDADES_VALIDAS:
            raise ValueError("Prioridad no valida")

        self.ticket_id = ticket_id
        self.solicitante = solicitante
        self.prioridad = prioridad
        self.estado = "ABIERTO"


def main() -> None:
    ticket = Ticket(1, "Ana Lopez", "alta")
    print(f"Ticket #{ticket.ticket_id} creado con estado {ticket.estado}")

    try:
        Ticket(2, "Luis Perez", "urgente")
    except ValueError as error:
        print(f"Error esperado: {error}")


if __name__ == "__main__":
    main()
