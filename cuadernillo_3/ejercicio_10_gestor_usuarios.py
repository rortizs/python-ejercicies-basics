"""Cuadernillo III - Ejercicio 10: Clase GestorUsuarios."""

class Usuario:
    def __init__(self, nombre: str, correo: str) -> None:
        self.nombre = nombre
        self.correo = correo


class GestorUsuarios:
    def __init__(self) -> None:
        self._usuarios: list[Usuario] = []

    def registrar_usuario(self, usuario: Usuario) -> None:
        self._usuarios.append(usuario)

    def buscar_por_correo(self, correo: str) -> Usuario | None:
        for usuario in self._usuarios:
            if usuario.correo == correo:
                return usuario
        return None


def main() -> None:
    gestor = GestorUsuarios()
    gestor.registrar_usuario(Usuario("Ana Lopez", "ana@umg.edu.gt"))

    encontrado = gestor.buscar_por_correo("ana@umg.edu.gt")
    print(encontrado.nombre if encontrado else None)

    no_encontrado = gestor.buscar_por_correo("nadie@umg.edu.gt")
    print(no_encontrado)


if __name__ == "__main__":
    main()
