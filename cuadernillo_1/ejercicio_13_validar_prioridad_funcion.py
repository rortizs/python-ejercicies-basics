"""Cuadernillo I - Ejercicio 13: Funcion reutilizable de validacion de prioridad."""

VALID_PRIORITIES = {"BAJA", "MEDIA", "ALTA"}


def validar_prioridad(prioridad: str) -> str | None:
    # Paso 1: normalizar el valor recibido
    normalized = prioridad.strip().upper()

    # Paso 2: devolver el valor normalizado si es valido, None si no
    if normalized in VALID_PRIORITIES:
        return normalized
    return None


def main() -> None:
    # Paso 3: probar la funcion con varios valores
    for sample in ("alta", "urgente", " media "):
        result = validar_prioridad(sample)
        print(f"validar_prioridad({sample!r}) -> {result!r}")


if __name__ == "__main__":
    main()
