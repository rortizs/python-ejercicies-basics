"""Ejemplo integrador: menu modular para registrar prestamos de biblioteca."""

#funcion para pedir la opcion del menu
def pedir_opcion() -> str: # -> str  indica que la funcion devuelve un string
    return input("\n1. Registrar\n2. Listar\n3. Resumen\n4. Buscar por estudiante\n0. Salir\nOpcion: ").strip() # strip() elimina los espacios al inicio y al final de lo que escribe el usuario

# funcion para registrar un prestamo
def registrar_prestamo(prestamos: list[dict[str, str]]) -> None: #dict[str, str] indica que el diccionario tiene claves y valores de tipo string, None indica que la funcion no devuelve nada
    estudiante = input("Estudiante: ").strip()
    libro = input("Libro: ").strip()
    #validacion de datos obligatorios
    if not estudiante or not libro:
        print("Los datos son obligatorios")
        return
    #agregar el prestamo a la lista de prestamos
    prestamos.append({"estudiante": estudiante, "libro": libro}) #append() agrega un elemento al final de la lista, en este caso un diccionario con los datos del prestamo

# funcion para listar los prestamos
def listar_prestamos(prestamos: list[dict[str, str]]) -> None:
    for indice, prestamo in enumerate(prestamos, start=1):
        print(f"{indice}. {prestamo['estudiante']} - {prestamo['libro']}")

# funcion para listar solamente los prestamos de un estudiante
def listar_prestamos_por_estudiante(prestamos: list[dict[str, str]], estudiante: str) -> None:
    encontrados = 0 # contador para saber si hubo resultados
    for indice, prestamo in enumerate(prestamos, start=1): #enumerate() devuelve un iterador que genera tuplas con el indice y el elemento de la lista, start=1 indica que el indice empieza en 1
        if prestamo['estudiante'].lower() == estudiante.lower(): #lower() en ambos lados para comparar sin distinguir mayusculas de minusculas
            print(f"{indice}. {prestamo['estudiante']} - {prestamo['libro']}")
            encontrados += 1
    if encontrados == 0:
        print("Sin prestamos para ese estudiante")

#funcion principal: repite el menu hasta que el usuario elige salir
def ejecutar_menu() -> None:
    prestamos: list[dict[str, str]] = []
    while True: #while es un bucle que se ejecuta mientras la condicion sea verdadera, break es una instruccion que termina el bucle
        opcion = pedir_opcion()
        if opcion == "1":
            registrar_prestamo(prestamos)
        elif opcion == "2":
            listar_prestamos(prestamos)
        elif opcion == "3":
            print({"prestamos_activos": len(prestamos)})
        elif opcion == "4":
            buscado = input("Estudiante a buscar: ").strip()
            listar_prestamos_por_estudiante(prestamos, buscado)
        elif opcion == "0":
            break #break es una instruccion que termina el bucle while
        else:
            print("Opcion no valida")

#if __name__ == "__main__": indica que el codigo se ejecuta solo si el archivo se corre directamente, no si se importa como modulo
if __name__ == "__main__":
    ejecutar_menu()
