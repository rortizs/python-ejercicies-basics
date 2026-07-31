"""Tema 5: operadores aritmeticos y de comparacion."""
# Los operadores aritmeticos se utilizan para realizar operaciones matematicas.
# Los operadores de comparacion se utilizan para comparar valores.
capacidad = 30
inscritos = 24
disponibles = capacidad - inscritos

print(f"Lugares disponibles: {disponibles}")
print(f"Curso lleno: {inscritos >= capacidad}") # >= devuelve un booleano: True o False


# el mismo ejemplo en c++
# int capacidad = 30;
# int inscritos = 24;
# int disponibles = capacidad - inscritos;
# std::cout << "Lugares disponibles: " << disponibles << std::endl;
# std::cout << "Curso lleno: " << (inscritos >= capacidad) << std::endl;

# el mismo ejemplo en c#
# int capacidad = 30;
# int inscritos = 24;
# int disponibles = capacidad - inscritos;
# Console.WriteLine($"Lugares disponibles: {disponibles}");
# Console.WriteLine($"Curso lleno: {inscritos >= capacidad}");
