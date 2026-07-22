#Conceptos base en python
#los archivos de python tienen la extension .py
#Qué nombre le pondrías a tu archivo de python? = CammelCase 'NombreArchivo.py', por ejemplo 'MiPrimerArchivo.py' |
# nombre_archivo.py, por ejemplo 'mi_primer_archivo.py' = ejemplo de snake_case, ejemplo incorrecto 'mi primer proyecto.py' = ejemplo de espacios en blanco, ejemplo incorrecto 'mi-primer-proyecto.py' = ejemplo de guiones, ejemplo incorrecto 'mi.primer.proyecto.py' = ejemplo de puntos, ejemplo incorrecto '
# comentarios en python se hacen con el símbolo #, todo lo que esté después del símbolo # será ignorado por el intérprete de python

# Variables y tipos de datos
# Una variable es un espacio en memoria que almacena un valor, el cual puede ser de
requester_name = "Ana López" # tipo de dato string
ticket_count = 3 # tipo de dato entero
estimated_hours = 1.5 # tipo de dato flotante
is_open = True # tipo de dato booleano, true o false, pero en python se escribe con mayúscula la primera letra, True o False


# c sharp como ejemplo para tipo de datos
# string requesterName var(20) = "Ana López"; // tipo de dato string, nombres, correos, descripciones, etc.
# int ticketCount = 3; // tipo de dato entero, números enteros, positivos

# Tipos basicos usados en python
# type str = "Ana López" # tipo de dato string, nombres, correos, descripciones, etc.
# type int = 3 # tipo de dato entero, números enteros, positivos o negativos
# type float = 1.5 # tipo de dato flotante, números decimales
# type bool = True # tipo de dato booleano, True o False
# type list = [1, 2, 3] # tipo de dato lista, colección de elementos | []
# type dict = {"key": "value"} # tipo de dato diccionario, colección de pares clave-valor | {}

# Entrada y salida de datos
requester_name = input("Nombre del solicitante: ") # input() es una función que permite al usuario ingresar datos por teclado
print(f"Solicitante registrado: {requester_name}") # print() es una función que permite mostrar datos en pantalla, f"" es una cadena de formato que permite insertar variables dentro de la cadena

# el input()n siempre devuelve un tipo de dato string (str). Si se necesita un número, se convierte:
age = int(input("Edad del solicitante: ")) # int() es una función que convierte un valor a tipo de dato entero
print(f"Edad del solicitante: {age}") # print() es una función que permite mostrar datos en pantalla, f"" es una cadena de formato que permite insertar variables dentro de la cadena

