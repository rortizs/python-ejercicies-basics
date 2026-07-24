"""Cuadernillo III - Ejercicio 8: Diagrama UML de la jerarquía completa."""

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
        return f"{super().describir()} - Tecnico en {self.especialidad}"


class Solicitante(Usuario):
    def __init__(self, nombre: str, correo: str, area_academica: str) -> None:
        super().__init__(nombre, correo)
        self.area_academica = area_academica

    def describir(self) -> str:
        return f"{super().describir()} - Solicitante de {self.area_academica}"


if __name__ == "__main__":
    print("Diagrama UML: Usuario <|-- Tecnico, Usuario <|-- Solicitante")
