# requester_capture.py

requester_name = input("Nombre del solicitante: ").strip()
requester_email = input("Correo institucional: ").strip().lower()
academic_area = input("Área o laboratorio: ").strip().upper()

print("\nFicha del solicitante")
print("---------------------")
print(f"Nombre: {requester_name}")
print(f"Correo: {requester_email}")
print(f"Área: {academic_area}")
