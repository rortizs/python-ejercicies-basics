"""Los metodos expresan el comportamiento de cada objeto."""


class Contador:
    def __init__(self) -> None:
        self.valor = 0

    def incrementar(self) -> None:
        self.valor += 1


contador = Contador()
contador.incrementar()
print(contador.valor)
