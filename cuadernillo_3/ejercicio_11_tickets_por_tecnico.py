"""Cuadernillo III - Ejercicio 11: GestorTickets.tickets_por_tecnico()."""

class Usuario:
    def __init__(self, nombre: str, correo: str) -> None:
        self.nombre = nombre
        self.correo = correo


class Tecnico(Usuario):
    def __init__(self, nombre: str, correo: str, especialidad: str) -> None:
        super().__init__(nombre, correo)
        self.especialidad = especialidad


class Ticket:
    PRIORIDADES_VALIDAS = {"BAJA", "MEDIA", "ALTA"}

    def __init__(self, ticket_id: int, solicitante: Usuario, prioridad: str) -> None:
        prioridad = prioridad.strip().upper()
        if prioridad not in self.PRIORIDADES_VALIDAS:
            raise ValueError("Prioridad no valida")

        self.ticket_id = ticket_id
        self.solicitante = solicitante
        self.prioridad = prioridad
        self.estado = "ABIERTO"
        self.tecnico_asignado: Tecnico | None = None

    def asignar_tecnico(self, tecnico: Tecnico) -> None:
        self.tecnico_asignado = tecnico
        self.estado = "EN_PROCESO"


class GestorTickets:
    def __init__(self) -> None:
        self._tickets: list[Ticket] = []

    def agregar_ticket(self, ticket: Ticket) -> None:
        self._tickets.append(ticket)

    def tickets_por_tecnico(self, tecnico: Tecnico) -> list[Ticket]:
        return [ticket for ticket in self._tickets if ticket.tecnico_asignado is tecnico]


def main() -> None:
    ana = Usuario("Ana Lopez", "ana@umg.edu.gt")
    luis = Tecnico("Luis Perez", "luis@umg.edu.gt", "Redes")
    marco = Tecnico("Marco Ruiz", "marco@umg.edu.gt", "Software")

    ticket_1 = Ticket(1, ana, "ALTA")
    ticket_1.asignar_tecnico(luis)
    ticket_2 = Ticket(2, ana, "MEDIA")
    ticket_2.asignar_tecnico(marco)
    ticket_3 = Ticket(3, ana, "BAJA")
    ticket_3.asignar_tecnico(luis)

    gestor = GestorTickets()
    for ticket in (ticket_1, ticket_2, ticket_3):
        gestor.agregar_ticket(ticket)

    for ticket in gestor.tickets_por_tecnico(luis):
        print(ticket.ticket_id)


if __name__ == "__main__":
    main()
