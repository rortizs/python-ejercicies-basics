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

# Limpieza de cadenas
raw_priority =  " alta " # cadena con espacios en blanco al inicio y al final
priority = raw_priority.strip().upper() # strip() es una función que elimina los espacios en blanco al inicio y al final de la cadena, upper() es una función que convierte la cadena a mayúsculas
print(priority) # print() es una función que permite mostrar datos en pantalla, f"" es una cadena de formato que permite insertar variables dentro de la cadena
#resultado esperado: ALTA

# Metodos de cadenas
#strip() #elimina los espacios en blanco al inicio y al final de la cadena
#upper() #convierte la cadena a mayúsculas 
#lower() #convierte la cadena a minúsculas 
name_upper = requester_name.upper() # upper() es una función que convierte la cadena a mayúsculas
name_lower = requester_name.lower() # lower() es una función que convierte la cadena a min


# Condiciones y operadores
priority = "ALTA" 
if priority == "ALTA": # if es una estructura de control que permite ejecutar un bloque de código si se cumple una condición
    print("El ticket debe antenderse con urgencia") # print() es una función que permite mostrar datos en pantalla, f"" es una cadena de formato que permite insertar variables dentro de la cadena
else: # else es una estructura de control que permite ejecutar un bloque de código si no se cumple la condición del if
    print("El ticket puede seguir el flujo normal") # print() es una función que permite mostrar datos en pantalla, f"" es una cadena de formato que permite insertar variables dentro de la cadena
    
# condicon negativa
priority = "BAJA"
if priority != "ALTA": # if es una estructura de control que permite ejecutar un bloque de código si se cumple una condición, != es un operador de comparación que significa "diferente a"
    print("El ticket puede seguir el flujo normal") # print() es una función que permite mostrar datos en pantalla, f"" es una cadena de formato que permite insertar variables dentro de la cadena   
else: # else es una estructura de control que permite ejecutar un bloque de código si no se cumple la condición del if
    print("El ticket debe antenderse con urgencia") # print() es una función que permite mostrar datos en pantalla, f"" es una cadena de formato que permite insertar variables dentro de la cadena
  
#diferencia ente == y =, == es un operador de comparación que significa "igual a", = es un operador de asignación que significa "asignar un valor a una variable"

# Listas y diccionarios
# Un ticket temporal puede representarse como un diccionario:
ticket = {
    "id_ticket": 1, # id del ticket, tipo de dato entero
    "requester": "Ana López", # nombre del solicitante, tipo de dato string
    "priority": "ALTA", # prioridad del ticket, tipo de dato string
    "status": "ABIERTO" # estado del ticket, tipo de dato string
}

# varios tickets pueden guardarse en una lista:
tickets = []
tickets.append(ticket) # append() es una función que permite agregar un elemento al final de la lista

#ciclos en python 
for ticket in tickets: # for es una estructura de control que permite ejecutar un bloque de código varias veces, ticket es una variable que representa cada elemento de la lista tickets
  print(ticket["id"], ticket["requester"], ticket["priority"], ticket["status"]) # print() es una función que permite mostrar datos en pantalla, f"" es una cadena de formato que permite insertar variables dentro de la cadena
  
# funcinoes en python
def normalize_priority(raw_priority: str) -> str: # def es una palabra reservada que permite definir una función, normalize_priority es el nombre de la función, raw_priority es un parámetro de la función, : str indica que el parámetro es de tipo string, -> str indica que la función devuelve un valor de tipo string
    """Normaliza la prioridad del ticket""" # """ """ es un comentario de varias líneas que describe la función
    return raw_priority.strip().upper() # return es una palabra reservada que permite devolver un valor desde la función, strip() es una función que elimina los espacios en blanco al inicio y al final de la cadena, upper() es una función que convierte la cadena a mayúsculas

#Errores Básicos
#Un programa profresional no debe aceptar cualquier tipo de dato, por ejemplo, si se espera un número entero, no se debe aceptar un string. Para evitar errores, se pueden usar condicionales y excepciones.
# ejemplo Una descripcion vacia
description = input("Descripción del ticket: ").strip() # input() es una función que permite al usuario ingresar datos por teclado, strip() es una función que elimina los espacios en blanco al inicio y al final de la cadena

if description == "": # if es una estructura de control que permite ejecutar un bloque de código si se cumple una condición, == es un operador de comparación que significa "igual a"
    print("Error: La descripción del ticket no puede estar vacía") # print() es una función que permite mostrar datos en pantalla, f"" es una cadena de formato que permite insertar variables dentro de la cadena
else: # else es una estructura de control que permite ejecutar un bloque de código si no se cumple la condición del if
    print("Descripcion aceptada") # print() es una función que permite mostrar datos en pantalla, f"" es una cadena de formato que permite insertar variables dentro de la cadena

