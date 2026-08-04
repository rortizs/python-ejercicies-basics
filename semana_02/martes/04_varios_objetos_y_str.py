"""Varios objetos comparten estructura, pero conservan estado propio."""

# Se crea una clase Libro con dos atributos: codigo y titulo.
class Libro:
    #funcion especial que permite inicializar los atributos del objeto al momento de crearlo.
    def __init__(self, codigo: str, titulo: str) -> None:
        self.codigo = codigo
        self.titulo = titulo

    # funcion especial que permite representar el objeto como una cadena de texto.
    def __str__(self) -> str:
        return f"{self.codigo}: {self.titulo}" #f para formatear la cadena de texto con los atributos del objeto.

# Se crean dos objetos de la clase Libro con diferentes valores para los atributos codigo y titulo.
libro_a = Libro("L-01", "El principito")
libro_b = Libro("L-02", "Momo")

print(libro_a)
print(libro_b)
print("Son objetos distintos:", libro_a is not libro_b) # is operador ==, is not operador !=, compara si los objetos son distintos.

