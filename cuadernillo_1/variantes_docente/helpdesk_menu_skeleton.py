# helpdesk_menu_skeleton.py

ALLOWED_PRIORITIES = ["BAJA", "MEDIA", "ALTA"]
INITIAL_STATUS = "ABIERTO"


def normalize_text(value: str) -> str:
    return value.strip()


def normalize_priority(value: str) -> str:
    return value.strip().upper()


def is_valid_priority(priority: str) -> bool:
    return priority in ALLOWED_PRIORITIES


def create_ticket(next_ticket_id: int) -> dict[str, str | int] | None:
    requester = normalize_text(input("Nombre del solicitante: "))
    email = normalize_text(input("Correo institucional: ")).lower()
    description = normalize_text(input("Descripción del problema: "))
    priority = normalize_priority(input("Prioridad (BAJA/MEDIA/ALTA): "))

    if requester == "":
        print("Error: el solicitante no puede estar vacío.")
        return None

    if description == "":
        print("Error: la descripción no puede estar vacía.")
        return None

    if not is_valid_priority(priority):
        print("Error: prioridad no válida.")
        return None

    return {
        "id": next_ticket_id,
        "requester": requester,
        "email": email,
        "description": description,
        "priority": priority,
        "status": INITIAL_STATUS,
    }


def list_tickets(tickets: list[dict[str, str | int]]) -> None:
    if len(tickets) == 0:
        print("No hay tickets registrados.")
        return

    print("\nTickets registrados")
    print("-------------------")
    for ticket in tickets:
        print(
            f"#{ticket['id']} | {ticket['requester']} | "
            f"{ticket['priority']} | {ticket['status']}"
        )


def find_ticket_by_id(
    tickets: list[dict[str, str | int]],
    ticket_id: int,
) -> dict[str, str | int] | None:
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket
    return None


def show_statistics(tickets: list[dict[str, str | int]]) -> None:
    total = len(tickets)
    high_priority = 0

    for ticket in tickets:
        if ticket["priority"] == "ALTA":
            high_priority += 1

    print("\nEstadísticas")
    print("------------")
    print(f"Total de tickets: {total}")
    print(f"Tickets de prioridad ALTA: {high_priority}")


def main() -> None:
    tickets: list[dict[str, str | int]] = []
    next_ticket_id = 1

    while True:
        print("\nHelpDesk EDU")
        print("1. Registrar ticket")
        print("2. Listar tickets")
        print("3. Buscar ticket por ID")
        print("4. Mostrar estadísticas")
        print("0. Salir")

        option = input("Seleccione una opción: ").strip()

        if option == "1":
            ticket = create_ticket(next_ticket_id)
            if ticket is not None:
                tickets.append(ticket)
                print(f"Ticket #{next_ticket_id} registrado.")
                next_ticket_id += 1
        elif option == "2":
            list_tickets(tickets)
        elif option == "3":
            try:
                ticket_id = int(input("ID del ticket: "))
            except ValueError:
                print("Error: el ID debe ser un número entero.")
                continue

            ticket = find_ticket_by_id(tickets, ticket_id)
            if ticket is None:
                print("Ticket no encontrado.")
            else:
                print(f"Ticket encontrado: {ticket}")
        elif option == "4":
            show_statistics(tickets)
        elif option == "0":
            print("Saliendo de HelpDesk EDU.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
