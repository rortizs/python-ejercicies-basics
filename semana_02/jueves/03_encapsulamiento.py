"""El guion bajo comunica que un atributo es de uso interno."""


class CuentaPuntos:
    def __init__(self) -> None:
        self._puntos = 0

    def agregar(self, cantidad: int) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self._puntos += cantidad

    def consultar(self) -> int:
        return self._puntos


cuenta = CuentaPuntos()
cuenta.agregar(10)
print(cuenta.consultar())
