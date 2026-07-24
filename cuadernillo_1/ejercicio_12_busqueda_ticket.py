"""Cuadernillo I - Ejercicio 12: Busqueda de ticket por ID."""

def main() -> None:
    # Paso 1: lista de tickets ya cargada (cada uno un diccionario)
    tickets = [
        {"id": 1, "requester": "Ana Lopez", "status": "ABIERTO"},
        {"id": 2, "requester": "Luis Perez", "status": "RESUELTO"},
    ]

    # Paso 2: pedir el id a buscar
    raw_id = input("ID del ticket a buscar: ").strip()
    try:
        ticket_id = int(raw_id)
    except ValueError:
        print("Error: el ID debe ser numerico.")
        return

    # Paso 3: busqueda lineal
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            print(f"Ticket #{ticket['id']} - {ticket['requester']} - {ticket['status']}")
            return

    # Paso 4: informar si no se encontro
    print("Ticket no encontrado.")


if __name__ == "__main__":
    main()
