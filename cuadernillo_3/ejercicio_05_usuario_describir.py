"""Cuadernillo III - Ejercicio 5: Clase Usuario consolidada con describir()."""

class Usuario:
    def __init__(self, nombre: str, correo: str) -> None:
        self.nombre = nombre
        self.correo = correo

    def describir(self) -> str:
        return f"{self.nombre} ({self.correo})"


def main() -> None:
    usuario = Usuario("Ana Lopez", "ana@umg.edu.gt")
    print(usuario.describir())


if __name__ == "__main__":
    main()
