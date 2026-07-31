"""Tema 4: input y conversion de texto a numero."""
# Para ejecutar un programa de Python se usa el comando python3 seguido de la ruta del archivo.
# Windows:   C:\Users\Usuario\curso_programacionII> python ejercicios\semana_01\martes\02_entrada_y_conversion.py
# Linux/Mac: usuario@equipo:~/curso_programacionII$ python3 ejercicios/semana_01/martes/02_entrada_y_conversion.py

# Forma sugerida de organizar su workspace (por ejemplo C:\Users\Usuario\Workspace):
# -- Python\Basico\
# -- BackEnd\
# -- FrontEnd\
# -- fullstack\
# -- Tools\


#input() permite al usuario ingresar datos desde la consola.
nombre = input("Nombre del estudiante: ").strip() # strip() elimina los espacios en blanco al inicio y al final de la cadena de texto ingresada por el usuario.

# try except permite manejar errores de conversion de datos.
try:
    # Intenta convertir la entrada a un número entero
    creditos = int(input("Creditos inscritos: "))
# except ValueError: esta es la forma de manejar el error si la conversion falla
except ValueError:
    print("Entrada invalida: los creditos deben ser un numero entero")
# else: si la conversion es exitosa, se ejecuta el bloque de codigo dentro del else
else:
    print(f"{nombre} inscribio {creditos} creditos")
