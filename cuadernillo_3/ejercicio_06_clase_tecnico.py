"""Cuadernillo III - Ejercicio 6: Clase Tecnico(Usuario)."""

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


def main() -> None:
    tecnico = Tecnico("Luis Perez", "luis@umg.edu.gt", "Redes")
    print(tecnico.describir())


if __name__ == "__main__":
    main()
