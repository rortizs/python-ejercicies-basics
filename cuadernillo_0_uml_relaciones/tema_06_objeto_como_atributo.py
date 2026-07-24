"""Cuadernillo 0 - UML y Relaciones - Tema 6: Composición/agregación en código: un objeto como atributo de otro."""

class Usuario:
    def __init__(self, nombre: str, correo: str) -> None:
        self.nombre = nombre
        self.correo = correo


class Ticket:
    def __init__(self, ticket_id: int, solicitante: Usuario, prioridad: str) -> None:
        self.ticket_id = ticket_id
        self.solicitante = solicitante  # objeto Usuario, no un string
        self.prioridad = prioridad


usuario = Usuario("Ana Lopez", "ana@umg.edu.gt")
ticket = Ticket(1, usuario, "ALTA")
print(ticket.solicitante.nombre)
