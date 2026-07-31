"""Tema 15: funciones, parametros, retorno y funciones booleanas."""
#def (definir una funcion) nombre_funcion(parametros):

#funcion para calcular el promedio de una lista de notas
def calcular_promedio(notas: list[float]) -> float: # -> float indica que la funcion devuelve un decimal
    return sum(notas) / len(notas) if notas else 0.0 #en una sola linea, si la lista de notas no esta vacia, devuelve la suma de las notas dividida entre la cantidad de notas, si esta vacia devuelve 0.0

#funcion para determinar si el promedio es mayor o igual a 61
def aprobo(promedio: float) -> bool: # -> bool indica que la funcion devuelve True o False
    return promedio >= 61

# print() para mostrar el promedio y si aprobo o no
promedio = calcular_promedio([75, 68, 80])
print(promedio, aprobo(promedio))


# la misma funcion escrita en otros lenguajes
#c#  float CalcularPromedio(List<float> notas) { return notas.Count > 0 ? notas.Sum() / notas.Count : 0.0f; }
#c++ float calcular_promedio(std::vector<float> notas) { /* recorrer el vector y dividir entre su tamaño */ }
#php function calcular_promedio($notas) { return count($notas) > 0 ? array_sum($notas) / count($notas) : 0.0; }
