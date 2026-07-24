"""Cuadernillo 0 - UML y Relaciones - Tema 14: isinstance() para distinguir el tipo real de un objeto."""

class Usuario:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre


class Tecnico(Usuario):
    pass


class Solicitante(Usuario):
    pass


usuarios: list[Usuario] = [Tecnico("Luis"), Solicitante("Ana"), Tecnico("Marco")]

tecnicos = sum(1 for usuario in usuarios if isinstance(usuario, Tecnico))
print(f"Cantidad de tecnicos: {tecnicos}")
