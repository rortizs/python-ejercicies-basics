"""Cuadernillo I - Ejercicio 9: Listado de tickets en memoria."""

def main() -> None:
    tickets: list[str] = []

    # Paso 1: registrar 3 tickets como resumen de texto
    for _ in range(3):
        requester = input("Nombre del solicitante: ").strip()
        description = input("Descripcion del problema: ").strip()
        tickets.append(f"{requester}: {description}")

    # Paso 2: mostrar el listado numerado
    print("\nTickets registrados:")
    for index, ticket in enumerate(tickets, start=1):
        print(f"{index}. {ticket}")


if __name__ == "__main__":
    main()
