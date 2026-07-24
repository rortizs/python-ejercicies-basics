"""Cuadernillo IV - Ejercicio 2: SQL básico: INSERT, SELECT y JOIN."""

import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, nombre TEXT)")
cursor.execute("CREATE TABLE tickets (id INTEGER PRIMARY KEY, titulo TEXT, requester_id INTEGER)")

cursor.execute("INSERT INTO users (nombre) VALUES ('Ana Lopez')")
cursor.execute("INSERT INTO tickets (titulo, requester_id) VALUES ('No enciende', 1)")
connection.commit()

cursor.execute("""
    SELECT tickets.titulo, users.nombre
    FROM tickets
    JOIN users ON tickets.requester_id = users.id
""")
for fila in cursor.fetchall():
    print(fila)

connection.close()
