"""Cuadernillo 0 - UML y Relaciones - Tema 11: Extender un método del padre con super().metodo()."""

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
        base = super().describir()  # reutiliza la version del padre...
        return f"{base} - Tecnico en {self.especialidad}"  # ...y agrega algo mas


tecnico = Tecnico("Luis Perez", "luis@umg.edu.gt", "Redes")
print(tecnico.describir())
