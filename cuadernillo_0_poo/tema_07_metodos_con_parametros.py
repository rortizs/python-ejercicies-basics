"""Cuadernillo 0 - POO - Tema 7: Metodos que reciben parametros ademas de self."""

class Ticket:
    def __init__(self, requester: str) -> None:
        self.requester = requester
        self.comments: list[str] = []

    def agregar_comentario(self, texto: str) -> None:
        self.comments.append(texto)


ticket = Ticket("Ana Lopez")
ticket.agregar_comentario("Se reviso el equipo")
print(ticket.comments)
