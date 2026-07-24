"""Cuadernillo III - Ejercicio 4: Diagrama UML de la relación Ticket–Comentario."""

# Este ejercicio es de diseno UML; el codigo abajo son las clases ya
# implementadas en el Ejercicio 3, que el diagrama debe representar fielmente.

class Ticket:
    def __init__(self) -> None:
        self.comentarios: list = []  # Ticket "1" o-- "0..*" Comentario


class Comentario:
    pass


if __name__ == "__main__":
    print("Diagrama UML: Ticket \"1\" o-- \"0..*\" Comentario : comentarios")
