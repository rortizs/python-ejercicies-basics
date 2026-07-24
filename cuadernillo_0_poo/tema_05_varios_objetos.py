"""Cuadernillo 0 - POO - Tema 5: Crear varios objetos de la misma clase."""

class Ticket:
    def __init__(self, requester: str, priority: str) -> None:
        self.requester = requester
        self.priority = priority


tickets = [
    Ticket("Ana Lopez", "ALTA"),
    Ticket("Luis Perez", "MEDIA"),
]
for ticket in tickets:
    print(f"{ticket.requester}: {ticket.priority}")
