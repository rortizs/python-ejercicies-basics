"""Cuadernillo I - Ejercicio 2: Registro del solicitante."""

def main() -> None:
    # Paso 1: capturar nombre y correo, limpiando espacios sobrantes
    requester = input("Nombre del solicitante: ").strip()
    email = input("Correo institucional: ").strip()

    # Paso 2: mostrar el resumen con los datos capturados
    print(f"Solicitante registrado: {requester} ({email})")


if __name__ == "__main__":
    main()
