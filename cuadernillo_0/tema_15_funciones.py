"""Cuadernillo 0 - Tema 15: Funciones: def, parametros, return y funciones booleanas."""

def es_mayor_de_edad(edad: int) -> bool:
    return edad >= 18


def saludar(nombre: str) -> str:
    return f"Hola, {nombre}"


print(es_mayor_de_edad(20))
print(saludar("Ana"))
