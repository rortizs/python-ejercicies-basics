"""Cuadernillo 0 - Tema 4: input() y conversion de tipos."""

texto = input("Ingrese su edad: ")
try:
    edad = int(texto)
    print(f"El proximo ano tendra {edad + 1} anos")
except ValueError:
    print("Error: debe ingresar un numero entero")
