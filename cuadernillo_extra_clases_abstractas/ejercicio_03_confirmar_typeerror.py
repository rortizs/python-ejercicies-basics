"""Cuadernillo Extra - Clases Abstractas - Ejercicio 3: Confirmar que Usuario ya no se puede instanciar directo."""

from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, nombre: str, correo: str) -> None:
        self.nombre = nombre
        self.correo = correo

    @abstractmethod
    def describir(self) -> str:
        ...


def main() -> None:
    try:
        Usuario("Juan", "juan@umg.edu.gt")
    except TypeError as error:
        print(f"Error esperado: {error}")


if __name__ == "__main__":
    main()
