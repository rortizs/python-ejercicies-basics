"""Cuadernillo Extra - Clases Abstractas - Ejercicio 5: Implementar Solicitante(Usuario) con el método obligatorio."""

from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, nombre: str, correo: str) -> None:
        self.nombre = nombre
        self.correo = correo

    @abstractmethod
    def describir(self) -> str:
        ...


class Solicitante(Usuario):
    def __init__(self, nombre: str, correo: str, area_academica: str) -> None:
        super().__init__(nombre, correo)
        self.area_academica = area_academica

    def describir(self) -> str:
        return f"{self.nombre} - Solicitante de {self.area_academica}"


def main() -> None:
    solicitante = Solicitante("Ana Lopez", "ana@umg.edu.gt", "Sistemas")
    print(solicitante.describir())


if __name__ == "__main__":
    main()
