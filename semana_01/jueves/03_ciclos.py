"""Temas 11 y 12: while centinela, for y acumuladores."""

#lista vacia de notas
notas = []
#while True: se repite indefinidamente hasta que el usuario escriba el centinela "fin"
while True:
    entrada = input("Nota (o fin): ").strip().lower() # strip() elimina espacios al inicio y al final, lower() convierte a minúsculas
    if entrada == "fin":
        break
    #try except para manejar errores de conversion de tipo
    try:
        nota = float(entrada) #float() convierte una cadena a un número decimal, int() convierte una cadena a un número entero
    #ValueError es la excepción que se lanza cuando la cadena no representa un número válido
    except ValueError:
        print("Nota invalida: ingrese un numero o escriba fin")
        continue
    notas.append(nota)

total = 0.0 # variable para acumular la suma de las notas
for indice in range(len(notas)): #range() genera una secuencia de números, len() devuelve la cantidad de elementos de la lista
    total += notas[indice] # += es un operador de asignación que suma el valor de la derecha al valor de la izquierda y asigna el resultado a la variable de la izquierda
#"if notas:" es equivalente a "if len(notas) > 0:" y evita dividir entre cero
if notas:
    print(f"Promedio: {total / len(notas):.2f}") # total / len(notas) calcula el promedio, :.2f formatea el número a 2 decimales
