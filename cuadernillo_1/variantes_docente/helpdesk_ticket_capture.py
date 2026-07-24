# helpdesk_ticket_capture.py

ALLOWED_PRIORITIES = ["BAJA", "MEDIA", "ALTA"]


def read_required_text(label: str) -> str:
    while True:
        value = input(label).strip()
        if value != "":
            return value
        print("Este campo es obligatorio.")


def read_priority() -> str:
    while True:
        priority = input("Prioridad (BAJA/MEDIA/ALTA): ").strip().upper()
        if priority in ALLOWED_PRIORITIES:
            return priority
        print("Prioridad no válida. Use BAJA, MEDIA o ALTA.")


def main() -> None:
    ticket = {
        "id": 1,
        "requester": read_required_text("Solicitante: "),
        "email": read_required_text("Correo: ").lower(),
        "description": read_required_text("Descripción: "),
        "priority": read_priority(),
        "status": "ABIERTO",
    }

    print("\nTicket listo para revisión")
    print("--------------------------")
    for key, value in ticket.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
