"""Cuadernillo I - Ejercicio 4: Normalizacion de texto del ticket."""

def main() -> None:
    # Paso 1: capturar la categoria tal como la escribe el usuario
    raw_category = input("Categoria del ticket: ")

    # Paso 2: normalizar quitando espacios y pasando a mayusculas
    normalized_category = raw_category.strip().upper()

    # Paso 3: mostrar el antes y el despues
    print(f"Categoria original: {raw_category!r}")
    print(f"Categoria normalizada: {normalized_category}")


if __name__ == "__main__":
    main()
