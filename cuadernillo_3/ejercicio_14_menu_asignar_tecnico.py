"""Cuadernillo III - Ejercicio 14: Integrar asignación de técnico al menú."""

class Usuario:
    def __init__(self, nombre: str, correo: str) -> None:
        self.nombre = nombre
        self.correo = correo


class Tecnico(Usuario):
    def __init__(self, nombre: str, correo: str, especialidad: str) -> None:
        super().__init__(nombre, correo)
        self.especialidad = especialidad


class Ticket:
    ESTADOS_VALIDOS = {"ABIERTO", "EN_PROCESO", "RESUELTO"}
    PRIORIDADES_VALIDAS = {"BAJA", "MEDIA", "ALTA"}

    def __init__(self, ticket_id: int, solicitante: Usuario, prioridad: str) -> None:
        prioridad = prioridad.strip().upper()
        if prioridad not in self.PRIORIDADES_VALIDAS:
            raise ValueError("Prioridad no valida")

        self.ticket_id = ticket_id
        self.solicitante = solicitante
        self.prioridad = prioridad
        self.estado = "ABIERTO"
        self.tecnico_asignado: Tecnico | None = None

    def asignar_tecnico(self, tecnico: Tecnico) -> None:
        self.tecnico_asignado = tecnico
        self.estado = "EN_PROCESO"


class GestorUsuarios:
    def __init__(self) -> None:
        self._usuarios: list[Usuario] = []

    def registrar_usuario(self, usuario: Usuario) -> None:
        self._usuarios.append(usuario)

    def buscar_por_correo(self, correo: str) -> Usuario | None:
        for usuario in self._usuarios:
            if usuario.correo == correo:
                return usuario
        return None


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


def asignar_tecnico_a_ticket(gestor_tickets: GestorTickets, gestor_usuarios: GestorUsuarios) -> None:
    raw_id = input("ID del ticket: ").strip()
    if not raw_id.isdigit():
        print("Error: el ID debe ser numerico.")
        return

    ticket = gestor_tickets.buscar_por_id(int(raw_id))
    if ticket is None:
        print("Ticket no encontrado.")
        return

    correo = input("Correo del tecnico: ").strip()
    tecnico = gestor_usuarios.buscar_por_correo(correo)
    if not isinstance(tecnico, Tecnico):
        print("Tecnico no encontrado.")
        return

    ticket.asignar_tecnico(tecnico)
    print(f"Ticket #{ticket.ticket_id} asignado a {tecnico.nombre}.")


def main() -> None:
    ana = Usuario("Ana Lopez", "ana@umg.edu.gt")
    luis = Tecnico("Luis Perez", "luis@umg.edu.gt", "Redes")

    gestor_usuarios = GestorUsuarios()
    gestor_usuarios.registrar_usuario(ana)
    gestor_usuarios.registrar_usuario(luis)

    gestor_tickets = GestorTickets()
    gestor_tickets.agregar_ticket(Ticket(1, ana, "ALTA"))

    asignar_tecnico_a_ticket(gestor_tickets, gestor_usuarios)

    ticket = gestor_tickets.buscar_por_id(1)
    print(ticket.tecnico_asignado.nombre, ticket.estado)


if __name__ == "__main__":
    main()
