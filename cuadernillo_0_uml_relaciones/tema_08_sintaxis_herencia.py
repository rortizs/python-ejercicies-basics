"""Cuadernillo 0 - UML y Relaciones - Tema 8: Sintaxis de herencia en Python: class Hija(Padre)."""

class Usuario:
    def __init__(self, nombre: str, correo: str) -> None:
        self.nombre = nombre
        self.correo = correo


class Tecnico(Usuario):
    pass


tecnico = Tecnico("Luis Perez", "luis@umg.edu.gt")
print(tecnico.nombre)  # heredado de Usuario, sin repetir codigo
