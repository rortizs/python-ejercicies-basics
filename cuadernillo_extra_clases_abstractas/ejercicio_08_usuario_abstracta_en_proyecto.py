"""Cuadernillo Extra - Clases Abstractas - Ejercicio 8: Proyecto Integrador: Usuario abstracta en HelpDesk EDU."""

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
        return f"{self.nombre} ({self.correo}) - Tecnico en {self.especialidad}"


class Solicitante(Usuario):
    def __init__(self, nombre: str, correo: str, area_academica: str) -> None:
        super().__init__(nombre, correo)
        self.area_academica = area_academica

    def describir(self) -> str:
        return f"{self.nombre} ({self.correo}) - Solicitante de {self.area_academica}"


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
    gestor.registrar_usuario(Tecnico("Luis Perez", "luis@umg.edu.gt", "Redes"))
    gestor.registrar_usuario(Solicitante("Ana Lopez", "ana@umg.edu.gt", "Sistemas"))

    for correo in ("luis@umg.edu.gt", "ana@umg.edu.gt"):
        usuario = gestor.buscar_por_correo(correo)
        print(usuario.describir())

    try:
        Usuario("Juan", "juan@umg.edu.gt")
    except TypeError as error:
        print(f"Error esperado: {error}")


if __name__ == "__main__":
    main()
