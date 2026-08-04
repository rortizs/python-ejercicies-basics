"""__init__ recibe self y establece atributos de instancia."""


class Libro:
    def __init__(self, titulo: str, autor: str, direccion: str, editorial: str, anio: int) -> None: # __init__ es un método especial que se llama automáticamente cuando se crea un objeto de la clase. Se utiliza para inicializar los atributos del objeto. El primer parámetro self hace referencia al objeto que se está creando, y los parámetros titulo y autor son los atributos que se van a establecer para ese objeto.
        self.titulo = titulo # self.titulo es un atributo de instancia que se establece con el valor del parámetro titulo. El atributo de instancia es una variable que pertenece a un objeto específico y puede tener un valor diferente para cada objeto.
        self.autor = autor
        self.direccion = direccion
        self.editorial = editorial
        self.anio = anio
        
#Libros es una lista de objetos de la clase Libro. Cada objeto se crea llamando al constructor de la clase Libro y pasando los valores de titulo y autor como argumentos. Luego, se recorre la lista de libros y se imprime el titulo y el autor de cada libro utilizando los atributos de instancia self.titulo y self.autor.

#class Libro, y mi lista Libros 
libros = [Libro("El principito", "Antoine de Saint-Exupery", "Calle 1", "Editorial 1", 1943), Libro("1984", "George Orwell", "Calle 2", "Editorial 2", 1948), Libro("Cien años de soledad", "Gabriel García Márquez", "Calle 3", "Editorial 3", 1967), Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Calle 4", "Editorial 4", 1605), Libro("La Odisea", "Homero", "Calle 5", "Editorial 5", -800)]
for libro in libros:
    print(libro.titulo, libro.autor)
    

#Ejercicio Linea blanca. Crear una clase llamada Electrodomestico que identifique el nombre, marca, modelo y precio de un electrodoméstico. Crear dos objetos de la clase Electrodomestico y verificar si son iguales o no.
#Cuando estamos creando un objeto de la clase siempre es importante tener claro los atributos que queremos que tenga ese objeto. En este caso, los atributos son nombre, marca, modelo y precio. Por lo tanto, el constructor de la clase Electrodomestico debe recibir estos parámetros y asignarlos a los atributos de instancia del objeto.

#Plantenamiento del Problema: Un cliente dandonos o presentado el poblema que tiene y que necesita que nosotros resolvamos con un programa. 
class Electrodomestico:
    def __init__(self, nombre: str, marca: str, modelo: str, linea: str, precio: float, sku: str, color: str) -> None:
        self.nombre = nombre
        self.marca = marca
        self.modelo = modelo
        self.linea = linea
        self.precio = precio
        self.sku = sku
        self.color = color
        
Electrodomesticos = [Electrodomestico("Refrigerador", "Samsung", "RT38K5982SL", "Samsung Bespoke", 12000.00, "SKU12345", "Plateado"), Electrodomestico("Lavadora", "LG", "WT19WBP6", "ThinQ", 8000.00, "SKU67890", "Blanco")]

for electrodomestico in Electrodomesticos:
    print(electrodomestico.nombre, electrodomestico.marca, electrodomestico.modelo, electrodomestico.linea, electrodomestico.precio, electrodomestico.sku, electrodomestico.color)  
    
    
      