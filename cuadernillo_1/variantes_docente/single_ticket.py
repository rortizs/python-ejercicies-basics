# single_ticket.py

allowed_priorities = ["BAJA", "MEDIA", "ALTA"]

ticket_id = 1
requester_name = input("Nombre del solicitante: ").strip()
requester_email = input("Correo institucional: ").strip().lower()
description = input("Descripción del problema: ").strip()
priority = input("Prioridad (BAJA/MEDIA/ALTA): ").strip().upper()

if description == "":
    print("Error: la descripción no puede estar vacía.")
elif priority not in allowed_priorities:
    print("Error: prioridad no válida.")
else:
    ticket = {
        "id": ticket_id,
        "requester": requester_name,
        "email": requester_email,
        "description": description,
        "priority": priority,
        "status": "ABIERTO",
    }

    print("\nTicket registrado")
    print("-----------------")
    print(f"ID: {ticket['id']}")
    print(f"Solicitante: {ticket['requester']}")
    print(f"Correo: {ticket['email']}")
    print(f"Descripción: {ticket['description']}")
    print(f"Prioridad: {ticket['priority']}")
    print(f"Estado: {ticket['status']}")
