"""Temas 6 y 7: cadenas, f-strings y metodos de texto."""

categoria = "  LABORATORIO  "
categoria_normalizada = categoria.strip().lower() # strip() elimina espacios al inicio y al final, lower() convierte a minúsculas

# la 'f' antes de las comillas significa "format": permite insertar variables dentro de {llaves}
print(f"Categoria: {categoria_normalizada}")
# len() devuelve la cantidad de caracteres de la cadena
print(f"Caracteres: {len(categoria_normalizada)}")
# upper() convierte la cadena a mayúsculas
print(f"Categoria en mayusculas: {categoria_normalizada.upper()}")
