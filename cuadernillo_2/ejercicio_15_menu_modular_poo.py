"""Cuadernillo II - Ejercicio 15: Mini proyecto integrador: HelpDesk EDU orientado a objetos."""

class Ticket:
    ESTADOS_VALIDOS = {"ABIERTO", "EN_PROCESO", "RESUELTO"}
    PRIORIDADES_VALIDAS = {"BAJA", "MEDIA", "ALTA"}

    def __init__(self, ticket_id: int, solicitante: str, prioridad: str) -> None:
        prioridad = self._normalizar(prioridad)
        if prioridad not in self.PRIORIDADES_VALIDAS:
            raise ValueError("Prioridad no valida")

        self.ticket_id = ticket_id
        self.solicitante = solicitante
        self.prioridad = prioridad
        self.estado = "ABIERTO"

    def _normalizar(self, valor: str) -> str:
        return valor.strip().upper()

    def mostrar_resumen(self) -> None:
        print(self)

    def cambiar_estado(self, nuevo_estado: str) -> bool:
        nuevo_estado = self._normalizar(nuevo_estado)
        if nuevo_estado not in self.ESTADOS_VALIDOS:
            return False
        self.estado = nuevo_estado
        return True

    def cambiar_prioridad(self, nueva_prioridad: str) -> bool:
        nueva_prioridad = self._normalizar(nueva_prioridad)
        if nueva_prioridad not in self.PRIORIDADES_VALIDAS:
            return False
        self.prioridad = nueva_prioridad
        return True

    def mismo_solicitante(self, otro: "Ticket") -> bool:
        return self.solicitante == otro.solicitante

    def __str__(self) -> str:
        return f"#{self.ticket_id} | {self.solicitante} | {self.prioridad} | {self.estado}"


class GestorTickets:
    def __init__(self) -> None:
        self._tickets: list[Ticket] = []

    def agregar_ticket(self, ticket: Ticket) -> None:
        self._tickets.append(ticket)

    def buscar_por_id(self, ticket_id: int) -> Ticket | None:
        for ticket in self._tickets:
            if ticket.ticket_id == ticket_id:
                return ticket
        return None

    def listar_tickets(self) -> None:
        if not self._tickets:
            print("No hay tickets registrados.")
            return
        for ticket in self._tickets:
            print(ticket)

    def estadisticas_por_prioridad(self) -> dict[str, int]:
        conteo = {"BAJA": 0, "MEDIA": 0, "ALTA": 0}
        for ticket in self._tickets:
            conteo[ticket.prioridad] += 1
        return conteo


def mostrar_menu() -> None:
    print("\nHelpDesk EDU (POO)")
    print("1. Registrar ticket")
    print("2. Listar tickets")
    print("3. Buscar ticket por ID")
    print("4. Ver estadisticas por prioridad")
    print("5. Salir")


def main() -> None:
    gestor = GestorTickets()
    next_id = 1

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            solicitante = input("Solicitante: ").strip()
            prioridad = input("Prioridad (BAJA/MEDIA/ALTA): ").strip()
            try:
                ticket = Ticket(next_id, solicitante, prioridad)
            except ValueError as error:
                print(f"Error: {error}")
                continue
            gestor.agregar_ticket(ticket)
            print(f"Ticket #{next_id} registrado.")
            next_id += 1
        elif opcion == "2":
            gestor.listar_tickets()
        elif opcion == "3":
            raw_id = input("ID del ticket: ").strip()
            if not raw_id.isdigit():
                print("Error: el ID debe ser numerico.")
                continue
            ticket = gestor.buscar_por_id(int(raw_id))
            print(ticket if ticket else "Ticket no encontrado.")
        elif opcion == "4":
            print(gestor.estadisticas_por_prioridad())
        elif opcion == "5":
            print("Saliendo de HelpDesk EDU.")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
