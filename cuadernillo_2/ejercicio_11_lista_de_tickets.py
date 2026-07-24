"""Cuadernillo II - Ejercicio 11: Lista de objetos Ticket."""

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
        print(self)

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

    def mismo_solicitante(self, otro: "Ticket") -> bool:
        return self.solicitante == otro.solicitante

    def __str__(self) -> str:
        return f"#{self.ticket_id} | {self.solicitante} | {self.prioridad} | {self.estado}"


def main() -> None:
    tickets = [
        Ticket(1, "Ana Lopez", "ALTA"),
        Ticket(2, "Luis Perez", "MEDIA"),
        Ticket(3, "Carla Diaz", "BAJA"),
        Ticket(4, "Marco Ruiz", "ALTA"),
    ]

    for ticket in tickets:
        print(ticket)


if __name__ == "__main__":
    main()
