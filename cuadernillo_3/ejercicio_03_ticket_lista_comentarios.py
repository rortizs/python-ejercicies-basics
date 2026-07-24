"""Cuadernillo III - Ejercicio 3: Ticket con lista de comentarios (agregación uno a muchos)."""

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


def main() -> None:
    usuario = Usuario("Ana Lopez", "ana@umg.edu.gt")
    ticket = Ticket(1, usuario, "ALTA")

    ticket.agregar_comentario(Comentario(usuario, "Primer seguimiento"))
    ticket.agregar_comentario(Comentario(usuario, "Segundo seguimiento"))

    print(len(ticket.comentarios))
    for comentario in ticket.comentarios:
        print(comentario)


if __name__ == "__main__":
    main()
