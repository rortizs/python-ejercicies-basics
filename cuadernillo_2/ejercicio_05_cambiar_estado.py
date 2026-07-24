"""Cuadernillo II - Ejercicio 5: Método cambiar_estado() con validación."""

class Ticket:
    ESTADOS_VALIDOS = {"ABIERTO", "EN_PROCESO", "RESUELTO"}
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

    def cambiar_estado(self, nuevo_estado: str) -> bool:
        nuevo_estado = nuevo_estado.strip().upper()
        if nuevo_estado not in self.ESTADOS_VALIDOS:
            return False
        self.estado = nuevo_estado
        return True


def main() -> None:
    ticket = Ticket(1, "Ana Lopez", "ALTA")
    print(ticket.cambiar_estado("en_proceso"))
    ticket.mostrar_resumen()
    print(ticket.cambiar_estado("pausado"))
    ticket.mostrar_resumen()


if __name__ == "__main__":
    main()
