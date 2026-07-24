"""Cuadernillo II - Ejercicio 14: Estadísticas dentro de GestorTickets."""

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


class GestorTickets:
    def __init__(self) -> None:
        self._tickets: list[Ticket] = []

    def agregar_ticket(self, ticket: Ticket) -> None:
        self._tickets.append(ticket)

    def buscar_por_id(self, ticket_id: int) -> Ticket | None:
        for ticket in self._tickets:
            if ticket.ticket_id == ticket_id:
                return ticket
        return None

    def listar_tickets(self) -> None:
        if not self._tickets:
            print("No hay tickets registrados.")
            return
        for ticket in self._tickets:
            print(ticket)

    def estadisticas_por_prioridad(self) -> dict[str, int]:
        conteo = {"BAJA": 0, "MEDIA": 0, "ALTA": 0}
        for ticket in self._tickets:
            conteo[ticket.prioridad] += 1
        return conteo


def main() -> None:
    gestor = GestorTickets()
    print(gestor.estadisticas_por_prioridad())

    gestor.agregar_ticket(Ticket(1, "Ana Lopez", "ALTA"))
    gestor.agregar_ticket(Ticket(2, "Luis Perez", "ALTA"))
    gestor.agregar_ticket(Ticket(3, "Carla Diaz", "BAJA"))

    print(gestor.estadisticas_por_prioridad())


if __name__ == "__main__":
    main()
