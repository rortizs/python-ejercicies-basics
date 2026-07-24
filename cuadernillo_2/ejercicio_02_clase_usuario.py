"""Cuadernillo II - Ejercicio 2: Clase Usuario con atributos básicos."""

class Usuario:
    def __init__(self, nombre: str, correo: str, rol: str) -> None:
        self.nombre = nombre
        self.correo = correo
        self.rol = rol


def main() -> None:
    usuario_1 = Usuario("Ana Lopez", "ana@umg.edu.gt", "solicitante")
    usuario_2 = Usuario("Luis Perez", "luis@umg.edu.gt", "tecnico")

    for usuario in (usuario_1, usuario_2):
        print(f"{usuario.nombre} ({usuario.rol}) - {usuario.correo}")


if __name__ == "__main__":
    main()
