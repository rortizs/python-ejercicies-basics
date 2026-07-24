"""Cuadernillo II - Ejercicio 8: Abstracción con un método privado de normalización."""

class Ticket:
    ESTADOS_VALIDOS = {"ABIERTO", "EN_PROCESO", "RESUELTO"}
    PRIORIDADES_VALIDAS = {"BAJA", "MEDIA", "ALTA"}

    def __init__(self, ticket_id: int, solicitante: str, prioridad: str) -> None:
        prioridad = self._normalizar(prioridad)
        if prioridad not in self.PRIORIDADES_VALIDAS:
            raise ValueError("Prioridad no valida")

        self.ticket_id = ticket_id
        self.solicitante = solicitante
        self.prioridad = prioridad
        self.estado = "ABIERTO"

    def _normalizar(self, valor: str) -> str:
        return valor.strip().upper()

    def mostrar_resumen(self) -> None:
        print(f"#{self.ticket_id} | {self.solicitante} | {self.prioridad} | {self.estado}")

    def cambiar_estado(self, nuevo_estado: str) -> bool:
        nuevo_estado = self._normalizar(nuevo_estado)
        if nuevo_estado not in self.ESTADOS_VALIDOS:
            return False
        self.estado = nuevo_estado
        return True

    def cambiar_prioridad(self, nueva_prioridad: str) -> bool:
        nueva_prioridad = self._normalizar(nueva_prioridad)
        if nueva_prioridad not in self.PRIORIDADES_VALIDAS:
            return False
        self.prioridad = nueva_prioridad
        return True


def main() -> None:
    ticket = Ticket(1, "Ana Lopez", " alta ")
    print(ticket.prioridad)
    print(ticket.cambiar_estado(" en_proceso "))
    print(ticket.estado)


if __name__ == "__main__":
    main()
