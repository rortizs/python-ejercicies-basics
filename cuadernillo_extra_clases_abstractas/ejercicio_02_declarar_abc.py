"""Cuadernillo Extra - Clases Abstractas - Ejercicio 2: Declarar Usuario como clase abstracta."""

from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, nombre: str, correo: str) -> None:
        self.nombre = nombre
        self.correo = correo

    @abstractmethod
    def describir(self) -> str:
        ...


if __name__ == "__main__":
    print("Usuario declarada como clase abstracta, sin errores al definirla.")
