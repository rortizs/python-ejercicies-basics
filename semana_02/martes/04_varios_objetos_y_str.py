"""Varios objetos comparten estructura, pero conservan estado propio."""


class Libro:
    def __init__(self, codigo: str, titulo: str) -> None:
        self.codigo = codigo
        self.titulo = titulo

    def __str__(self) -> str:
        return f"{self.codigo}: {self.titulo}"


libro_a = Libro("L-01", "El principito")
libro_b = Libro("L-02", "Momo")

print(libro_a)
print(libro_b)
print("Son objetos distintos:", libro_a is not libro_b)
