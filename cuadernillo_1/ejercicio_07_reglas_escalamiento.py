"""Cuadernillo I - Ejercicio 7: Reglas combinadas de escalamiento."""

def main() -> None:
    # Paso 1: capturar categoria y prioridad, normalizando ambos
    category = input("Categoria del ticket: ").strip().upper()
    priority = input("Prioridad del ticket: ").strip().upper()

    # Paso 2: aplicar la regla de escalamiento combinando condiciones
    if category == "INFRAESTRUCTURA" and priority == "ALTA":
        print("Ticket escalado a supervisor.")
    else:
        print("Ticket sigue el flujo normal.")


if __name__ == "__main__":
    main()
