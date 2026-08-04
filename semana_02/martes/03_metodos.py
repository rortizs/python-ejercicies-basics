"""Los metodos expresan el comportamiento de cada objeto."""


class Contador:
    def __init__(self) -> None:
        self.valor = 0

    def incrementar(self) -> None:
        self.valor += 1 # += en python suma el valor de la variable a la derecha con el valor de la variable a la izquierda y lo asigna a la variable de la izquierda.


contador = Contador() # Se crea un objeto de la clase Contador y se asigna a la variable contador.
contador.incrementar() # Se llama al metodo incrementar del objeto contador, lo que incrementa el valor de la variable valor en 1.
print(contador.valor) # Se imprime el valor de la variable valor del objeto contador, que es 1.


#ejercicio: Crear un metodo que reste 1 al valor del contador.
class Contador:
    def __init__(self) -> None:
        self.valor = 0

    def incrementar(self) -> None:
        self.valor += 2

    def decrementar(self) -> None:
        self.valor -= 1  # Se resta 1 al valor de la variable valor.

contador = Contador() # Se crea un objeto de la clase Contador y se asigna a la variable contador.
contador.incrementar() # Se llama al metodo incrementar del objeto contador, lo que incrementa el valor de la variable valor en 1.
contador.decrementar() # Se llama al metodo decrementar del objeto contador, lo que decrementa el valor de la variable valor en 1.
print(contador.valor) # Se imprime el valor de la variable valor del objeto contador, que es 1.