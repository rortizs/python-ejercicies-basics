"""Cuadernillo Extra - Clases Abstractas - Ejercicio 1: ¿Por qué existe una clase abstracta?."""

# Este ejercicio es de analisis. El codigo siguiente muestra el problema
# actual: nada impide crear un Usuario "generico" sin rol real.

class Usuario:
    def __init__(self, nombre: str, correo: str) -> None:
        self.nombre = nombre
        self.correo = correo


if __name__ == "__main__":
    generico = Usuario("Juan", "juan@umg.edu.gt")  # esto no deberia ser posible
    print(f"Se creo un Usuario sin rol: {generico.nombre}")
