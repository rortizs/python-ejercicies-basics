"""Cuadernillo IV - Ejercicio 1: Modelo entidad-relación: de clases a tablas."""

import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        correo TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE tickets (
        id INTEGER PRIMARY KEY,
        titulo TEXT NOT NULL,
        prioridad TEXT NOT NULL,
        requester_id INTEGER NOT NULL,
        FOREIGN KEY (requester_id) REFERENCES users(id)
    )
""")

cursor.execute("""
    CREATE TABLE comments (
        id INTEGER PRIMARY KEY,
        texto TEXT NOT NULL,
        ticket_id INTEGER NOT NULL,
        author_id INTEGER NOT NULL,
        FOREIGN KEY (ticket_id) REFERENCES tickets(id),
        FOREIGN KEY (author_id) REFERENCES users(id)
    )
""")

connection.commit()
print("3 tablas creadas: users, tickets, comments")
connection.close()
