"""Cuadernillo III - Ejercicio 9: Ticket.asignar_tecnico() — agregación Ticket–Tecnico."""

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

    def cambiar_estado(self, nuevo_estado: str) -> bool:
        nuevo_estado = nuevo_estado.strip().upper()
        if nuevo_estado not in self.ESTADOS_VALIDOS:
            return False
        self.estado = nuevo_estado
        return True

    def asignar_tecnico(self, tecnico: Tecnico) -> None:
        self.tecnico_asignado = tecnico
        self.cambiar_estado("en_proceso")


def main() -> None:
    ana = Usuario("Ana Lopez", "ana@umg.edu.gt")
    ticket = Ticket(1, ana, "ALTA")
    tecnico = Tecnico("Luis Perez", "luis@umg.edu.gt", "Redes")

    ticket.asignar_tecnico(tecnico)
    print(ticket.tecnico_asignado.nombre, ticket.estado)


if __name__ == "__main__":
    main()
