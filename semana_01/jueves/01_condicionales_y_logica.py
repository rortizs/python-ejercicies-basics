"""Temas 8 y 9: condicionales y operadores and, or, not."""

# condicionales y operadores lógicos
promedio = 61
asistencia = 80
tiene_justificacion = False #porque la variable tiene un valor booleano, no es necesario poner el '== True' o '== False'

#el promedio es mayor o igual a 61
cumple_promedio = promedio >= 61
#cumple asistencia si es mayor o igual a 80 o si tiene justificación
cumple_asistencia = asistencia >= 80 or tiene_justificacion

# si cumple ambas condiciones (and = las dos deben ser verdaderas)
if cumple_promedio and cumple_asistencia:
    #hago el print()
    print("Curso aprobado")
# o de lo contrario, si no cumple promedio y asistencia
elif not cumple_promedio and not cumple_asistencia:
    #hago el print()
    print("Curso no aprobado: promedio y asistencia insuficientes")
# o de lo contrario, si no cumple promedio
elif not cumple_promedio:
    #hago el print()
    print("Curso no aprobado: promedio insuficiente")
# o de lo contrario, si no cumple asistencia
else:
    print("Curso no aprobado: asistencia insuficiente")


#la misma logica encapsulada en una funcion: recibe los datos por parametro y devuelve el mensaje
def determinar_aprobacion(cumple_promedio: bool, cumple_asistencia: bool) -> str:
    if cumple_promedio and cumple_asistencia:
        return "Curso aprobado"
    elif not cumple_promedio and not cumple_asistencia:
        return "Curso no aprobado: promedio y asistencia insuficientes"
    elif not cumple_promedio:
        return "Curso no aprobado: promedio insuficiente"
    else:
        return "Curso no aprobado: asistencia insuficiente"


print("Con funcion:", determinar_aprobacion(cumple_promedio, cumple_asistencia))
