"""Cuadernillo III - Ejercicio 15: Proyecto Integrador: HelpDesk EDU orientado a objetos completo."""

class Usuario:
    def __init__(self, nombre: str, correo: str) -> None:
        self.nombre = nombre
        self.correo = correo

    def describir(self) -> str:
        return f"{self.nombre} ({self.correo})"


class Tecnico(Usuario):
    def __init__(self, nombre: str, correo: str, especialidad: str) -> None:
        super().__init__(nombre, correo)
        self.especialidad = especialidad

    def describir(self) -> str:
        return f"{super().describir()} - Tecnico en {self.especialidad}"


class Solicitante(Usuario):
    def __init__(self, nombre: str, correo: str, area_academica: str) -> None:
        super().__init__(nombre, correo)
        self.area_academica = area_academica

    def describir(self) -> str:
        return f"{super().describir()} - Solicitante de {self.area_academica}"


class Comentario:
    def __init__(self, autor: Usuario, texto: str) -> None:
        texto = texto.strip()
        if not texto:
            raise ValueError("El comentario no puede estar vacio")
        self.autor = autor
        self.texto = texto

    def __str__(self) -> str:
        return f"{self.autor.nombre}: {self.texto}"


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
        self.comentarios: list[Comentario] = []

    def asignar_tecnico(self, tecnico: Tecnico) -> None:
        self.tecnico_asignado = tecnico
        self.estado = "EN_PROCESO"

    def agregar_comentario(self, comentario: Comentario) -> None:
        self.comentarios.append(comentario)

    def __str__(self) -> str:
        tecnico = self.tecnico_asignado.nombre if self.tecnico_asignado else "sin asignar"
        return (
            f"#{self.ticket_id} | {self.solicitante.nombre} | {self.prioridad} | "
            f"{self.estado} | tecnico: {tecnico} | comentarios: {len(self.comentarios)}"
        )


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
    print("\nHelpDesk EDU - Proyecto Integrador")
    print("1. Registrar usuario")
    print("2. Registrar ticket")
    print("3. Asignar tecnico")
    print("4. Agregar comentario")
    print("5. Listar tickets")
    print("6. Buscar ticket por ID")
    print("7. Ver estadisticas")
    print("8. Salir")


def main() -> None:
    gestor_usuarios = GestorUsuarios()
    gestor_tickets = GestorTickets()
    next_ticket_id = 1

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            nombre = input("Nombre: ").strip()
            correo = input("Correo: ").strip()
            tipo = input("Tipo (tecnico/solicitante): ").strip().lower()
            if tipo == "tecnico":
                especialidad = input("Especialidad: ").strip()
                usuario = Tecnico(nombre, correo, especialidad)
            else:
                area = input("Area academica: ").strip()
                usuario = Solicitante(nombre, correo, area)
            gestor_usuarios.registrar_usuario(usuario)
            print(f"Usuario registrado: {usuario.describir()}")

        elif opcion == "2":
            correo = input("Correo del solicitante: ").strip()
            solicitante = gestor_usuarios.buscar_por_correo(correo)
            if solicitante is None:
                print("Error: solicitante no encontrado.")
                continue
            prioridad = input("Prioridad (BAJA/MEDIA/ALTA): ").strip()
            try:
                ticket = Ticket(next_ticket_id, solicitante, prioridad)
            except ValueError as error:
                print(f"Error: {error}")
                continue
            gestor_tickets.agregar_ticket(ticket)
            print(f"Ticket #{next_ticket_id} registrado.")
            next_ticket_id += 1

        elif opcion == "3":
            raw_id = input("ID del ticket: ").strip()
            if not raw_id.isdigit():
                print("Error: el ID debe ser numerico.")
                continue
            ticket = gestor_tickets.buscar_por_id(int(raw_id))
            if ticket is None:
                print("Ticket no encontrado.")
                continue
            correo = input("Correo del tecnico: ").strip()
            tecnico = gestor_usuarios.buscar_por_correo(correo)
            if not isinstance(tecnico, Tecnico):
                print("Error: tecnico no encontrado.")
                continue
            ticket.asignar_tecnico(tecnico)
            print(f"Ticket #{ticket.ticket_id} asignado a {tecnico.nombre}.")

        elif opcion == "4":
            raw_id = input("ID del ticket: ").strip()
            if not raw_id.isdigit():
                print("Error: el ID debe ser numerico.")
                continue
            ticket = gestor_tickets.buscar_por_id(int(raw_id))
            if ticket is None:
                print("Ticket no encontrado.")
                continue
            correo = input("Correo del autor del comentario: ").strip()
            autor = gestor_usuarios.buscar_por_correo(correo)
            if autor is None:
                print("Error: autor no encontrado.")
                continue
            texto = input("Comentario: ")
            try:
                ticket.agregar_comentario(Comentario(autor, texto))
            except ValueError as error:
                print(f"Error: {error}")
                continue
            print("Comentario agregado.")

        elif opcion == "5":
            gestor_tickets.listar_tickets()

        elif opcion == "6":
            raw_id = input("ID del ticket: ").strip()
            if not raw_id.isdigit():
                print("Error: el ID debe ser numerico.")
                continue
            ticket = gestor_tickets.buscar_por_id(int(raw_id))
            print(ticket if ticket else "Ticket no encontrado.")

        elif opcion == "7":
            print(gestor_tickets.estadisticas_por_prioridad())

        elif opcion == "8":
            print("Saliendo de HelpDesk EDU.")
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
