"""Un metodo puede recibir parametros y devolver un resultado."""


class Producto:
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio

    def precio_con_descuento(self, porcentaje: float) -> float:
        return self.precio * (1 - porcentaje / 100)


producto = Producto("Cuaderno", 25.0)
print(producto.precio_con_descuento(10))
