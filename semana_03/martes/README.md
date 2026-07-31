# Martes: notacion de clases

Una **clase** describe las caracteristicas y operaciones comunes de un tipo de elemento. Un **objeto** es una instancia concreta de esa clase: `libro_a: Libro` y `libro_b: Libro` comparten el modelo, pero representan objetos distintos.

Para identificar clases en un enunciado, buscá conceptos con identidad y responsabilidades propias. Los datos que describen esos conceptos son candidatos a atributos; las acciones que les corresponden son candidatas a metodos. No todo sustantivo se convierte en clase: un color o una fecha suelen ser valores.

Una clase UML se divide en nombre, atributos y metodos. Por ahora, la visibilidad se usa solo para leer la notacion UML necesaria:

| Simbolo | Visibilidad |
| --- | --- |
| `+` | publica |
| `#` | protegida |
| `-` | privada |

```text
Libro
-------------------------
- codigo: str
# estado: str
+ titulo: str
-------------------------
+ prestar(): bool
+ devolver(): None
```

Las convenciones de acceso propias de Python se formalizaran mas adelante. Los simbolos UML no implican por si solos que Python impida el acceso a un atributo.

## Practica de identificacion

En una biblioteca, una persona solicita el prestamo de un ejemplar y una sede registra la operacion. Son buenos candidatos a clase `Persona`, `Prestamo`, `Ejemplar`, `Libro` y `Sede`. En cambio, `fecha_devolucion` es inicialmente un atributo de `Prestamo`.
