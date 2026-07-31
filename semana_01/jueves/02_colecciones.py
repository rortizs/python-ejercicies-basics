"""Temas 10, 13 y 14: conjuntos, listas y diccionarios."""
# colecciones, listas y diccionarios en python
codigos_permitidos = {"MAT", "FIS", "PRO"} # conjunto de códigos permitidos
cursos = ["Programacion II", "Fisica II", "Programacion II"] # lista de cursos, sus índices son 0, 1 y 2
#persistencia de los datos en una lista de diccionarios, donde cada diccionario tiene los datos de un estudiante
# diccionario de estudiante = {"id": "A-101", "nombre": "Ana", "cursos": cursos}
estudiantes = [
    {"id": "A-101", "nombre": "Ana", "cursos": cursos},
    {"id": "A-102", "nombre": "Luis", "cursos": ["Estadistica"]},
]
estudiante = estudiantes[0]

# Agregar un curso a la lista de cursos del estudiante
# ojo: "cursos" y estudiante["cursos"] son la MISMA lista, por eso el append tambien afecta a Ana
cursos.append("Matematica III") # append() agrega un elemento al final de la lista
print("PRO" in codigos_permitidos) # print() imprime en pantalla, 'in' verifica si un elemento está en un conjunto o lista
print(f"Programacion II aparece {cursos.count('Programacion II')} veces")
print(f"{estudiante['nombre']}: {len(estudiante['cursos'])} cursos")
for clave, valor in estudiante.items(): # items() devuelve una lista de tuplas con los pares clave-valor del diccionario
    print(clave, valor)

#buscar un estudiante por su ID

id_buscado = "A-102"
encontrado = None #none es un valor especial que indica que la variable no tiene ningún valor asignado
for candidato in estudiantes:
    if candidato["id"] == id_buscado: # == es un operador de comparación que verifica si dos valores son iguales, != es un operador de comparación que verifica si dos valores son diferentes
        encontrado = candidato
        break # break es una instrucción que termina el bucle for o while en el que se encuentra

print("Busqueda lineal:", encontrado)
