# multiple_tickets.py

allowed_priorities = ["BAJA", "MEDIA", "ALTA"]
tickets = []
next_ticket_id = 1

while True:
    print("\nRegistro de ticket")
    print("Escriba 0 en el nombre para salir.")

    requester_name = input("Nombre del solicitante: ").strip()
    if requester_name == "0":
        break

    requester_email = input("Correo institucional: ").strip().lower()
    description = input("Descripción del problema: ").strip()
    priority = input("Prioridad (BAJA/MEDIA/ALTA): ").strip().upper()

    if description == "":
        print("Error: la descripción no puede estar vacía.")
        continue

    if priority not in allowed_priorities:
        print("Error: prioridad no válida. Use BAJA, MEDIA o ALTA.")
        continue

    ticket = {
        "id": next_ticket_id,
        "requester": requester_name,
        "email": requester_email,
        "description": description,
        "priority": priority,
        "status": "ABIERTO",
    }

    tickets.append(ticket)
    print(f"Ticket #{next_ticket_id} registrado.")
    next_ticket_id += 1

print("\nTickets registrados")
print("-------------------")

if len(tickets) == 0:
    print("No se registraron tickets.")
else:
    for ticket in tickets:
        print(
            f"#{ticket['id']} | {ticket['requester']} | "
            f"{ticket['priority']} | {ticket['status']}"
        )
