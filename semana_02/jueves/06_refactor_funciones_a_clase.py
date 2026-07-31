"""Refactor progresivo: agrupar estado y operaciones relacionadas."""


def calcular_total(precios: list[float]) -> float:
    return sum(precios)


precios_iniciales = [12.0, 8.0]
print("Enfoque con funcion:", calcular_total(precios_iniciales))


class Canasta:
    def __init__(self) -> None:
        self._precios: list[float] = []

    def agregar(self, precio: float) -> None:
        if precio <= 0:
            raise ValueError("El precio debe ser positivo")
        self._precios.append(precio)

    def calcular_total(self) -> float:
        return sum(self._precios)


canasta = Canasta()
for precio in precios_iniciales:
    canasta.agregar(precio)
print("Enfoque con clase:", canasta.calcular_total())
