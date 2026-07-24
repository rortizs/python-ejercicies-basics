"""Cuadernillo III - Ejercicio 2: Método __str__ para Comentario."""

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


def main() -> None:
    usuario = Usuario("Ana Lopez", "ana@umg.edu.gt")
    comentario = Comentario(usuario, "Se reviso el equipo")
    print(comentario)


if __name__ == "__main__":
    main()
