"""Una clase define la estructura; cada objeto mantiene su identidad."""

# class libro: pass identifica la clase, no el objeto
class Libro:
    pass # pass es un marcador de posición, no hace nada


libro_a = Libro() #libro_a es un objeto de la clase Libro
libro_b = Libro() #libro_b es otro objeto de la clase Libro
print(type(libro_a)) #print(type(libro_a))
print(type(libro_b)) #print(type(libro_b))
print(libro_a is libro_b) #print(libro_a == libro_b) #False, son objetos distintos

# ejercicio: crear una clase llamada Persona, crear dos objetos de la clase Persona y verificar si son iguales o no.

class Persona:
    pass

persona_a = Persona() # Persona(), el parentesis indica que se está creando un objeto de la clase Persona
persona_b = Persona()
print(type(persona_a))
print(type(persona_b))
print(persona_a is persona_b)


# ejercicio: crear una clase llamada Coche, crear dos objetos de la clase Coche y verificar si son iguales o no.

class Coche:
    pass

coche_a = Coche()
coche_b = Coche()
print(type(coche_a))
print(type(coche_b))
print(coche_a is coche_b) 

#ejercicio: Crear una clase Usuario que identifique el nombre, apellidos, direccion y correo electrónico de un usuario. Crear dos objetos de la clase Usuario y verificar si son iguales o no.

class Usuario:
    pass

# nombre de usuario = ejemplo#1: Richard(PN) Oswaldo(SN) David(TN) Ortiz(AP) Sasvín(AM), search while  
usuario_primerNombre = Usuario()
usuario_segundoNombre = Usuario()
usuario_tercerNombre = Usuario()
usuario_cuartoNombre = Usuario()
usuario_ApellidoPaterno = Usuario()
usuario_ApellidoMaterno = Usuario()
#direccion, Calle, número, colonia, caserio, aldea, ciudad, estado, código postal
usuario_Direccion = Usuario() 
print(type(usuario_primerNombre))
print(type(usuario_segundoNombre))
print(type(usuario_tercerNombre))
print(type(usuario_cuartoNombre))
print(type(usuario_ApellidoPaterno))
print(type(usuario_ApellidoMaterno))
print(type(usuario_Direccion))
print(usuario_primerNombre is usuario_segundoNombre) #validar que el primer nombre y el segundo nombre no son iguales, ya que son objetos distintos

#ejercicio: Crear una clase llamada Animal que identifique el nombre, especie, edad y color de un animal. Crear dos objetos de la clase Animal y verificar si son iguales o no.
class Animal:
    pass

animal_a = Animal()
animal_b = Animal()
print(type(animal_a))
print(type(animal_b))
print(animal_a is animal_b)
 