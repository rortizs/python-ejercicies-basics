"""La abstraccion expone operaciones utiles y oculta detalles internos."""


class Carrito:
    def __init__(self) -> None:
        self._precios: list[float] = []

    def agregar_producto(self, precio: float) -> None:
        if precio <= 0:
            raise ValueError("El precio debe ser positivo")
        self._precios.append(precio)

    def total(self) -> float:
        return sum(self._precios)


carrito = Carrito()
carrito.agregar_producto(12.50)
carrito.agregar_producto(8.25)
print(carrito.total())
