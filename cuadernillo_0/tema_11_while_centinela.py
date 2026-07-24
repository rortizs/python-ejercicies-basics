"""Cuadernillo 0 - Tema 11: Ciclos while y el patron centinela."""

contador = 0
while True:
    dato = input("Ingrese un dato (0 para salir): ")
    if dato == "0":
        break
    contador += 1
print(f"Se ingresaron {contador} datos")
