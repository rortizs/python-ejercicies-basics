"""Atributos de clase, atributos de instancia y colecciones de objetos."""


class Producto:
    impuesto = 0.12

    def __init__(self, codigo: str, nombre: str, precio: float) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def mismo_codigo(self, otro: "Producto") -> bool:
        return self.codigo == otro.codigo

    def precio_final(self) -> float:
        return self.precio * (1 + self.impuesto)


productos = [
    Producto("P-01", "Cuaderno", 20.0),
    Producto("P-02", "Lapiz", 3.5),
]
producto_repetido = Producto("P-01", "Cuaderno grande", 28.0)

print("Impuesto compartido:", Producto.impuesto)
print("Mismo identificador:", productos[0].mismo_codigo(producto_repetido))
for producto in productos:
    print(producto.nombre, f"{producto.precio_final():.2f}")
