"""Cuadernillo I - Ejercicio 15: Mini proyecto integrador: menu modular de HelpDesk EDU."""

VALID_PRIORITIES = {"BAJA", "MEDIA", "ALTA"}


def mostrar_menu() -> None:
    # Paso 1: mostrar las opciones disponibles
    print("\nHelpDesk EDU")
    print("1. Registrar ticket")
    print("2. Listar tickets")
    print("3. Buscar ticket por ID")
    print("4. Ver estadisticas por prioridad")
    print("5. Salir")


def registrar_ticket(tickets: list[dict], next_id: int) -> int:
    # Paso 2: capturar y validar un nuevo ticket
    requester = input("Solicitante: ").strip()
    priority = input("Prioridad (BAJA/MEDIA/ALTA): ").strip().upper()

    if not requester or priority not in VALID_PRIORITIES:
        print("Error: datos invalidos, ticket no registrado.")
        return next_id

    tickets.append({"id": next_id, "requester": requester, "priority": priority})
    print(f"Ticket #{next_id} registrado.")
    return next_id + 1


def listar_tickets(tickets: list[dict]) -> None:
    # Paso 3: recorrer y mostrar todos los tickets
    if not tickets:
        print("No hay tickets registrados.")
        return
    for ticket in tickets:
        print(f"#{ticket['id']} | {ticket['requester']} | {ticket['priority']}")


def buscar_ticket(tickets: list[dict], ticket_id: int) -> None:
    # Paso 4: busqueda lineal por id
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            print(f"#{ticket['id']} | {ticket['requester']} | {ticket['priority']}")
            return
    print("Ticket no encontrado.")


def mostrar_estadisticas(tickets: list[dict]) -> None:
    # Paso 5: calcular porcentaje por prioridad, evitando division por cero
    total = len(tickets)
    if total == 0:
        print("No hay tickets registrados.")
        return
    for level in ("BAJA", "MEDIA", "ALTA"):
        count = sum(1 for t in tickets if t["priority"] == level)
        print(f"{level}: {round(count / total * 100, 1)}%")


def main() -> None:
    # Paso 6: ciclo principal del menu, integrando todas las funciones anteriores
    tickets: list[dict] = []
    next_id = 1

    while True:
        mostrar_menu()
        option = input("Seleccione una opcion: ").strip()

        if option == "1":
            next_id = registrar_ticket(tickets, next_id)
        elif option == "2":
            listar_tickets(tickets)
        elif option == "3":
            raw_id = input("ID del ticket: ").strip()
            if raw_id.isdigit():
                buscar_ticket(tickets, int(raw_id))
            else:
                print("Error: el ID debe ser numerico.")
        elif option == "4":
            mostrar_estadisticas(tickets)
        elif option == "5":
            print("Saliendo de HelpDesk EDU.")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
