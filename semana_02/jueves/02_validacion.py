"""El constructor protege al objeto de estados iniciales invalidos."""


class Curso:
    def __init__(self, nombre: str, cupo: int) -> None:
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("El nombre es obligatorio")
        if cupo <= 0:
            raise ValueError("El cupo debe ser positivo")
        self.nombre = nombre
        self.cupo = cupo


curso = Curso("Programacion II", 30)
print(curso.nombre, curso.cupo)
