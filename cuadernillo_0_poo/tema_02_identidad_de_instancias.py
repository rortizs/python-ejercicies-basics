"""Cuadernillo 0 - POO - Tema 2: Crear objetos e identidad de cada instancia."""

class Ticket:
    pass


ticket_a = Ticket()
ticket_b = Ticket()
print(ticket_a == ticket_b)  # False: son objetos distintos
print(ticket_a is ticket_a)  # True: es el mismo objeto
