"""Cuadernillo III - Ejercicio 13: Integrar comentarios al menú."""

class Usuario:
    def __init__(self, nombre: str, correo: str) -> None:
        self.nombre = nombre
        self.correo = correo


class Comentario:
    def __init__(self, autor: Usuario, texto: str) -> None:
        texto = texto.strip()
        if not texto:
            raise ValueError("El comentario no puede estar vacio")
        self.autor = autor
        self.texto = texto

    def __str__(self) -> str:
        return f"{self.autor.nombre}: {self.texto}"


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
        self.comentarios: list[Comentario] = []

    def agregar_comentario(self, comentario: Comentario) -> None:
        self.comentarios.append(comentario)


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


def comentar_ticket(gestor: GestorTickets, autor: Usuario) -> None:
    raw_id = input("ID del ticket a comentar: ").strip()
    if not raw_id.isdigit():
        print("Error: el ID debe ser numerico.")
        return

    ticket = gestor.buscar_por_id(int(raw_id))
    if ticket is None:
        print("Ticket no encontrado.")
        return

    texto = input("Comentario: ")
    try:
        ticket.agregar_comentario(Comentario(autor, texto))
    except ValueError as error:
        print(f"Error: {error}")
        return

    print("Comentario agregado.")


def main() -> None:
    ana = Usuario("Ana Lopez", "ana@umg.edu.gt")
    gestor = GestorTickets()
    gestor.agregar_ticket(Ticket(1, ana, "ALTA"))

    comentar_ticket(gestor, ana)
    comentar_ticket(gestor, ana)

    ticket = gestor.buscar_por_id(1)
    for comentario in ticket.comentarios:
        print(comentario)


if __name__ == "__main__":
    main()
