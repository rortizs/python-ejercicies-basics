"""Cuadernillo 0 - POO - Tema 9: Modificar atributos desde un metodo (encapsular una regla)."""

class Ticket:
    ESTADOS_VALIDOS = {"ABIERTO", "EN_PROCESO", "RESUELTO"}

    def __init__(self) -> None:
        self.estado = "ABIERTO"

    def cambiar_estado(self, nuevo_estado: str) -> bool:
        nuevo_estado = nuevo_estado.strip().upper()
        if nuevo_estado not in self.ESTADOS_VALIDOS:
            return False
        self.estado = nuevo_estado
        return True


ticket = Ticket()
print(ticket.cambiar_estado("en_proceso"))
print(ticket.estado)
