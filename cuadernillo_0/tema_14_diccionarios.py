"""Cuadernillo 0 - Tema 14: Diccionarios: crear, acceder por clave y recorrer."""

ticket = {"id": 1, "solicitante": "Ana", "prioridad": "ALTA"}
print(ticket["solicitante"])
for clave, valor in ticket.items():
    print(f"{clave}: {valor}")
