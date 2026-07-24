"""Cuadernillo I - Ejercicio 10: Conteo de tickets por estado."""

def main() -> None:
    # Paso 1: lista de estados ya cargada (simulando datos existentes)
    statuses = ["ABIERTO", "RESUELTO", "ABIERTO", "EN_PROCESO"]

    # Paso 2: acumuladores por estado
    open_count = 0
    in_progress_count = 0
    resolved_count = 0

    # Paso 3: recorrer y contar
    for status in statuses:
        if status == "ABIERTO":
            open_count += 1
        elif status == "EN_PROCESO":
            in_progress_count += 1
        elif status == "RESUELTO":
            resolved_count += 1

    # Paso 4: mostrar el resultado
    print(f"ABIERTO: {open_count}, EN_PROCESO: {in_progress_count}, RESUELTO: {resolved_count}")


if __name__ == "__main__":
    main()
