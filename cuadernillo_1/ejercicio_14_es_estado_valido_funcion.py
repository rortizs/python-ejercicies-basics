"""Cuadernillo I - Ejercicio 14: Funcion booleana de validacion de estado."""

VALID_STATUSES = {"ABIERTO", "EN_PROCESO", "RESUELTO"}


def es_estado_valido(estado: str) -> bool:
    # Paso 1: normalizar y comparar contra el catalogo permitido
    return estado.strip().upper() in VALID_STATUSES


def main() -> None:
    # Paso 2: probar la funcion con varios estados
    for sample in ("ABIERTO", "PAUSADO", "resuelto"):
        print(f"es_estado_valido({sample!r}) -> {es_estado_valido(sample)}")


if __name__ == "__main__":
    main()
