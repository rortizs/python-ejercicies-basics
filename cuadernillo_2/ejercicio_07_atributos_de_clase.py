"""Cuadernillo II - Ejercicio 7: Atributos de clase compartidos."""

class Ticket:
    ESTADOS_VALIDOS = {"ABIERTO", "EN_PROCESO", "RESUELTO"}  # atributo de clase: compartido, no cambia por objeto
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
    # Se accede desde la clase, no desde un objeto: no hace falta crear un Ticket para conocer el catalogo
    print(Ticket.ESTADOS_VALIDOS)
    print(Ticket.PRIORIDADES_VALIDAS)


if __name__ == "__main__":
    main()
