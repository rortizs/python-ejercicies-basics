"""__init__ recibe self y establece atributos de instancia."""


class Libro:
    def __init__(self, titulo: str, autor: str) -> None:
        self.titulo = titulo
        self.autor = autor


libros = [Libro("El principito", "Antoine de Saint-Exupery"), Libro("1984", "George Orwell")]
for libro in libros:
    print(libro.titulo, libro.autor)
