# Jueves: multiplicidad y maestro-detalle

La multiplicidad indica cuantos objetos pueden participar en cada extremo de una relacion.

| Notacion | Lectura |
| --- | --- |
| `1` | exactamente uno |
| `0..1` | cero o uno |
| `*` o `0..*` | cero o muchos |
| `1..*` | uno o muchos |

## Ejemplo maestro-detalle

```text
Orden 1 ---------------- 1..* DetalleOrden
```

`Orden` es el maestro y conserva numero, fecha y cliente. Cada `DetalleOrden` representa una linea con producto, cantidad, precio unitario y subtotal.

Se escoge `1..*` porque la invariante del modelo establece que una orden confirmada debe tener al menos un detalle. Si el sistema permitiera guardar borradores vacios, corresponderia `0..*`. La multiplicidad expresa una regla del dominio, no una preferencia grafica.

## Diagrama completo de dominio

```mermaid
classDiagram
    class Biblioteca
    class Sede
    class Seccion
    class Libro
    class Autor
    class Ejemplar
    class Persona
    class Prestamo
    class DetallePrestamo
    class Reserva
    class Categoria

    Biblioteca "1" -- "1..*" Sede
    Sede "1" -- "1..*" Seccion
    Seccion "1" -- "0..*" Ejemplar
    Libro "1" -- "0..*" Ejemplar
    Autor "0..*" -- "1..*" Libro
    Categoria "1" -- "0..*" Libro
    Persona "1" -- "0..*" Prestamo
    Prestamo "1" -- "1..*" DetallePrestamo
    DetallePrestamo "0..*" -- "1" Ejemplar
    Persona "1" -- "0..*" Reserva
    Reserva "0..*" -- "1" Libro
```

Este modelo contiene once clases. `Prestamo` y `DetallePrestamo` forman el ejemplo maestro-detalle: el maestro identifica a la persona y las fechas generales; cada detalle referencia un ejemplar. La naturaleza exacta de cada relacion y sus criterios de ciclo de vida se estudian en Semana 4.
