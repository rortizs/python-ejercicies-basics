"""Cuadernillo 0 - Tema 10: Conjuntos (set) y el operador in."""

ESTADOS_VALIDOS = {"ABIERTO", "EN_PROCESO", "RESUELTO"}
estado = "PAUSADO"
if estado not in ESTADOS_VALIDOS:
    print("Error: estado no reconocido")
