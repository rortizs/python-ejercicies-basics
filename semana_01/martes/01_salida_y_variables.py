"""Temas 1 a 3: print, comentarios, nombres, variables y tipos."""

# Un nombre claro comunica mejor que una abreviatura.
# Python distingue entre mayúsculas y minúsculas, por lo que "nombre" y "Nombre" son nombres distintos.
# Por convención (PEP 8), las variables en Python se escriben en snake_case: minúsculas y guion bajo.
nombre_curso = "Programacion II" # Nombre del curso
sesion = 1
esta_activa = True

print(nombre_curso) # print() muestra en pantalla el valor de la variable
print(type(sesion), type(esta_activa))

# Una cadena literal es la forma de representar datos de texto directamente en el código fuente. Se puede usar comillas simples o dobles.
# - Encerrado: Las cadenas deben estar encerradas entre comillas simples (' ') o dobles (" "). Python las trata por igual. Lo importante es ser coherente y usar siempre el mismo tipo de comillas para una cadena.
# - Contenido: Todo lo que se encuentra dentro de las comillas se considera parte de la cadena. Esto incluye letras, números, símbolos y espacios en blanco.
# - Propósito: Las cadenas se utilizan para representar texto en un programa. Pueden contener palabras, frases, oraciones o cualquier otro tipo de información textual.
# ejemplo:
saludo = "Hello World"
print(saludo)

# ejemplo 1: usar comillas dobles para definir una cadena
print("Hello, World!")  # Salida: Hello, World!

# ejemplo 2: usar comillas simples para definir una cadena
print('Python is fun!')  # Salida: Python is fun!

# ejemplo 3: cadena que contiene números y símbolos
print("123 Main Street #45")

# Por qué print() es fundamental por varias razones:
# 1. Salida: Es la forma principal de mostrar información al usuario o al desarrollador durante la ejecución del programa.
# 2. Depuración: A medida que escribes programas, print() te permite verificar el estado de las variables y el flujo del programa, ayudándote a identificar errores.
# 3. Interacción del Usuario: En programas más complejos, print() puede usarse para mostrar mensajes al usuario, instrucciones o resultados de cálculos.
