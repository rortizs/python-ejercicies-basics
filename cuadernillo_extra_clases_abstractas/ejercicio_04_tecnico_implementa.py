"""Cuadernillo Extra - Clases Abstractas - Ejercicio 4: Implementar Tecnico(Usuario) con el método obligatorio."""

from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, nombre: str, correo: str) -> None:
        self.nombre = nombre
        self.correo = correo

    @abstractmethod
    def describir(self) -> str:
        ...


class Tecnico(Usuario):
    def __init__(self, nombre: str, correo: str, especialidad: str) -> None:
        super().__init__(nombre, correo)
        self.especialidad = especialidad

    def describir(self) -> str:
        return f"{self.nombre} - Tecnico en {self.especialidad}"


def main() -> None:
    tecnico = Tecnico("Luis Perez", "luis@umg.edu.gt", "Redes")
    print(tecnico.describir())


if __name__ == "__main__":
    main()
