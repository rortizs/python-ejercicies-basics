"""Cuadernillo II - Ejercicio 4: Método mostrar_resumen()."""

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

    def mostrar_resumen(self) -> None:
        print(f"#{self.ticket_id} | {self.solicitante} | {self.prioridad} | {self.estado}")


def main() -> None:
    ticket = Ticket(1, "Ana Lopez", "ALTA")
    ticket.mostrar_resumen()


if __name__ == "__main__":
    main()
