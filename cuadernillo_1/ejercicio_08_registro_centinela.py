"""Cuadernillo I - Ejercicio 8: Registro de varios tickets con centinela."""

def main() -> None:
    ticket_count = 0

    # Paso 1: repetir la captura hasta que el solicitante escriba "0"
    while True:
        requester = input("Nombre del solicitante (0 para salir): ").strip()

        # Paso 2: condicion de salida (centinela)
        if requester == "0":
            break

        description = input("Descripcion del problema: ").strip()
        print(f"Ticket registrado para {requester}: {description}")

        # Paso 3: acumular el contador
        ticket_count += 1

    # Paso 4: reportar el total registrado
    print(f"Se registraron {ticket_count} tickets.")


if __name__ == "__main__":
    main()
