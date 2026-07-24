"""Cuadernillo I - Ejercicio 6: Validacion de prioridad del ticket."""

VALID_PRIORITIES = {"BAJA", "MEDIA", "ALTA"}


def main() -> None:
    # Paso 1: capturar la prioridad y normalizarla
    priority = input("Prioridad (BAJA/MEDIA/ALTA): ").strip().upper()

    # Paso 2: validar contra el catalogo permitido
    if priority not in VALID_PRIORITIES:
        print("Error: prioridad no valida.")
        return

    # Paso 3: confirmar
    print(f"Prioridad valida: {priority}")


if __name__ == "__main__":
    main()
