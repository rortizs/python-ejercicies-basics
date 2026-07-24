"""Cuadernillo III - Ejercicio 7: Clase Solicitante(Usuario)."""

class Usuario:
    def __init__(self, nombre: str, correo: str) -> None:
        self.nombre = nombre
        self.correo = correo

    def describir(self) -> str:
        return f"{self.nombre} ({self.correo})"


class Solicitante(Usuario):
    def __init__(self, nombre: str, correo: str, area_academica: str) -> None:
        super().__init__(nombre, correo)
        self.area_academica = area_academica

    def describir(self) -> str:
        return f"{super().describir()} - Solicitante de {self.area_academica}"


def main() -> None:
    solicitante = Solicitante("Ana Lopez", "ana@umg.edu.gt", "Sistemas")
    print(solicitante.describir())


if __name__ == "__main__":
    main()
