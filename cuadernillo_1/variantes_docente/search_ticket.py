# search_ticket.py

tickets = [
    {
        "id": 1,
        "requester": "Ana López",
        "email": "ana@edu.gt",
        "description": "El teclado del laboratorio 1 no funciona",
        "priority": "MEDIA",
        "status": "ABIERTO",
    },
    {
        "id": 2,
        "requester": "Luis García",
        "email": "luis@edu.gt",
        "description": "No hay internet en aula 204",
        "priority": "ALTA",
        "status": "ABIERTO",
    },
]

try:
    searched_id = int(input("ID del ticket a buscar: "))
except ValueError:
    print("Error: el ID debe ser un número entero.")
else:
    found_ticket = None

    for ticket in tickets:
        if ticket["id"] == searched_id:
            found_ticket = ticket
            break

    if found_ticket is None:
        print("No se encontró un ticket con ese ID.")
    else:
        print("\nTicket encontrado")
        print("-----------------")
        print(f"ID: {found_ticket['id']}")
        print(f"Solicitante: {found_ticket['requester']}")
        print(f"Correo: {found_ticket['email']}")
        print(f"Descripción: {found_ticket['description']}")
        print(f"Prioridad: {found_ticket['priority']}")
        print(f"Estado: {found_ticket['status']}")
