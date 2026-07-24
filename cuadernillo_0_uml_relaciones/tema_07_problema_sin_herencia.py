"""Cuadernillo 0 - UML y Relaciones - Tema 7: Herencia: qué es y por qué existe."""

class Tecnico:
    def __init__(self, nombre: str, correo: str, especialidad: str) -> None:
        self.nombre = nombre  # duplicado
        self.correo = correo  # duplicado
        self.especialidad = especialidad


class Solicitante:
    def __init__(self, nombre: str, correo: str, area_academica: str) -> None:
        self.nombre = nombre  # duplicado
        self.correo = correo  # duplicado
        self.area_academica = area_academica
