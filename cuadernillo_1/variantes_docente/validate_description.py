# validate_description.py

description = input("Describa el problema: ").strip()

if description == "":
    print("Error: la descripción no puede estar vacía.")
else:
    print("Descripción registrada correctamente.")
    print(f"Detalle: {description}")
