"""Cuadernillo 0 - POO - Tema 15: De la funcion a la clase: refactorizar codigo funcional."""

class Ticket:
    ESTADOS_VALIDOS = {"ABIERTO", "EN_PROCESO", "RESUELTO"}

    def __init__(self, ticket_id: int, requester: str, priority: str) -> None:
        self.ticket_id = ticket_id
        self.requester = requester
        self.priority = priority
        self.estado = "ABIERTO"

    def cambiar_estado(self, nuevo_estado: str) -> bool:
        nuevo_estado = nuevo_estado.strip().upper()
        if nuevo_estado not in self.ESTADOS_VALIDOS:
            return False
        self.estado = nuevo_estado
        return True

    def __str__(self) -> str:
        return f"#{self.ticket_id} | {self.requester} | {self.priority} | {self.estado}"


tickets = [Ticket(1, "Ana Lopez", "ALTA")]
for ticket in tickets:
    print(ticket)
