"""Cuadernillo Extra - Clases Abstractas - Ejercicio 6: ¿Qué pasa si una subclase no implementa el método abstracto?."""

from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, nombre: str, correo: str) -> None:
        self.nombre = nombre
        self.correo = correo

    @abstractmethod
    def describir(self) -> str:
        ...


class Supervisor(Usuario):
    pass  # no implementa describir() a proposito


def main() -> None:
    try:
        Supervisor("Ana", "ana@umg.edu.gt")
    except TypeError as error:
        print(f"Error esperado: {error}")


if __name__ == "__main__":
    main()
