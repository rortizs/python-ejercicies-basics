"""Cuadernillo I - Ejercicio 3: Captura de datos del primer ticket."""

def main() -> None:
    # Paso 1: capturar datos de texto
    requester = input("Nombre del solicitante: ").strip()
    description = input("Descripcion del problema: ").strip()

    # Paso 2: capturar y convertir el tiempo estimado (float), con manejo de error
    raw_time = input("Tiempo estimado de atencion (horas): ").strip()
    try:
        estimated_hours = float(raw_time)
    except ValueError:
        print("Error: debe ingresar un numero valido.")
        return

    # Paso 3: mostrar cada dato junto con su tipo
    print(f"Solicitante: {requester} ({type(requester).__name__})")
    print(f"Descripcion: {description} ({type(description).__name__})")
    print(f"Tiempo estimado: {estimated_hours} horas ({type(estimated_hours).__name__})")


if __name__ == "__main__":
    main()
