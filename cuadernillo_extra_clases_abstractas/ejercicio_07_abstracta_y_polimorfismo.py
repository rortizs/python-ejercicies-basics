"""Cuadernillo Extra - Clases Abstractas - Ejercicio 7: Clase abstracta + polimorfismo."""

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


class Solicitante(Usuario):
    def __init__(self, nombre: str, correo: str, area_academica: str) -> None:
        super().__init__(nombre, correo)
        self.area_academica = area_academica

    def describir(self) -> str:
        return f"{self.nombre} - Solicitante de {self.area_academica}"


def main() -> None:
    usuarios: list[Usuario] = [
        Tecnico("Luis Perez", "luis@umg.edu.gt", "Redes"),
        Solicitante("Ana Lopez", "ana@umg.edu.gt", "Sistemas"),
        Tecnico("Marco Ruiz", "marco@umg.edu.gt", "Software"),
        Solicitante("Carla Diaz", "carla@umg.edu.gt", "Enfermeria"),
    ]

    for usuario in usuarios:
        print(usuario.describir())


if __name__ == "__main__":
    main()
