"""Cuadernillo 0 - UML y Relaciones - Tema 9: super().__init__() para reutilizar el constructor del padre."""

class Usuario:
    def __init__(self, nombre: str, correo: str) -> None:
        self.nombre = nombre
        self.correo = correo


class Tecnico(Usuario):
    def __init__(self, nombre: str, correo: str, especialidad: str) -> None:
        super().__init__(nombre, correo)
        self.especialidad = especialidad


tecnico = Tecnico("Luis Perez", "luis@umg.edu.gt", "Redes")
print(tecnico.nombre, tecnico.especialidad)
