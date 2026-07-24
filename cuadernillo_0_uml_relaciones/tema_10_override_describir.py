"""Cuadernillo 0 - UML y Relaciones - Tema 10: Sobrescribir (override) un método heredado."""

class Usuario:
    def __init__(self, nombre: str, correo: str) -> None:
        self.nombre = nombre
        self.correo = correo

    def describir(self) -> str:
        return f"{self.nombre} ({self.correo})"


class Tecnico(Usuario):
    def __init__(self, nombre: str, correo: str, especialidad: str) -> None:
        super().__init__(nombre, correo)
        self.especialidad = especialidad

    def describir(self) -> str:
        return f"{self.nombre} - Tecnico en {self.especialidad}"


usuario = Usuario("Ana Lopez", "ana@umg.edu.gt")
tecnico = Tecnico("Luis Perez", "luis@umg.edu.gt", "Redes")
print(usuario.describir())
print(tecnico.describir())  # usa la version sobrescrita, no la del padre
