"""Cuadernillo I - Ejercicio 5: Validacion de campos obligatorios."""

def main() -> None:
    # Paso 1: capturar los tres campos obligatorios
    requester = input("Nombre del solicitante: ").strip()
    email = input("Correo institucional: ").strip()
    description = input("Descripcion del problema: ").strip()

    # Paso 2: validar que ninguno este vacio
    if not requester or not email or not description:
        print("Error: el nombre, el correo y la descripcion son obligatorios.")
        return

    # Paso 3: confirmar el registro
    print("Ticket registrado.")


if __name__ == "__main__":
    main()
