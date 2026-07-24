# validate_priority.py

allowed_priorities = ["BAJA", "MEDIA", "ALTA"]

priority = input("Prioridad del ticket (BAJA/MEDIA/ALTA): ").strip().upper()

if priority in allowed_priorities:
    print(f"Prioridad aceptada: {priority}")
else:
    print("Error: prioridad no válida.")
    print("Use solamente: BAJA, MEDIA o ALTA.")
