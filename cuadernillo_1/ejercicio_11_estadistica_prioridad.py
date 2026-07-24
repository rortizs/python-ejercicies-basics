"""Cuadernillo I - Ejercicio 11: Estadistica de prioridad."""

def main() -> None:
    # Paso 1: lista de prioridades ya cargada
    priorities = ["ALTA", "MEDIA", "ALTA", "BAJA"]

    # Paso 2: evitar division por cero
    total = len(priorities)
    if total == 0:
        print("No hay tickets registrados.")
        return

    # Paso 3: calcular porcentaje por prioridad
    for level in ("BAJA", "MEDIA", "ALTA"):
        count = priorities.count(level)
        percentage = round(count / total * 100, 1)
        print(f"{level}: {percentage}%")


if __name__ == "__main__":
    main()
