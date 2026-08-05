# UML del proyecto final (HelpDesk EDU) — Semana 3 y 4

Código PlantUML listo para copiar en el [editor online de PlantUML](https://www.plantuml.com/plantuml/uml/) o en la extensión de VS Code. Las clases y campos reflejan el modelo real de `help_desk_EDU/app/models/entities.py`, así que sirve como guía progresiva hacia la implementación de semanas posteriores.

## 1. Diagrama de clases completo

```plantuml
@startuml DiagramaClases_HelpDesk
skinparam classAttributeIconSize 0
hide circle

enum Role {
  ADMINISTRATOR
  SUPERVISOR
  TECHNICIAN
  REQUESTER
}

enum TicketStatus {
  OPEN
  IN_PROGRESS
  RESOLVED
  CLOSED
  CANCELLED
}

class User {
  -id: int
  -email: str
  -name: str
  -role: str
  -password_hash: str
  +verificarCredenciales(password: str): bool
}

class Ticket {
  -id: int
  -title: str
  -description: str
  -category: str
  -priority: str
  -status: str
  -createdAt: datetime
  -dueAt: datetime
  +asignar(tecnico: User): None
  +cambiarEstado(nuevoEstado: str): None
  +cancelar(): None
  +cerrar(): None
  +agregarComentario(autor: User, texto: str): Comment
}

class Comment {
  -id: int
  -body: str
  -createdAt: datetime
}

class History {
  -id: int
  -eventType: str
  -detail: str
  -createdAt: datetime
}

class Notification {
  -id: int
  -title: str
  -message: str
  -channel: str
  -type: str
  -readAt: datetime
  +marcarLeida(): None
}

class Article {
  -id: int
  -title: str
  -body: str
  -category: str
  -createdAt: datetime
}

User "1" -- "0..*" Ticket : solicita >
User "0..1" -- "0..*" Ticket : atiende >
Ticket "1" *-- "0..*" Comment : contiene
User "1" -- "0..*" Comment : autor >
Ticket "1" *-- "0..*" History : registra
User "1" -- "0..*" History : actor >
User "1" -- "0..*" Notification : recibe >
Ticket "0..1" -- "0..*" Notification : referencia >
User "1" -- "0..*" Article : publica >

User ..> Role : usa
Ticket ..> TicketStatus : usa
@enduml
```

Criterio de las relaciones: `Comment` y `History` no tienen sentido sin su `Ticket` (composición, rombo negro en `Ticket`). `Notification` y `Article` referencian a `User` pero conservan identidad propia (asociación). `Ticket.assignee` es opcional (`0..1`) porque un ticket puede estar sin asignar; `Ticket.requester` es obligatorio (`1`).

## 2. Diagramas de secuencia (4)

### 2.1 Iniciar sesión

```plantuml
@startuml SecuenciaLogin
actor Usuario
participant "Sistema HelpDesk" as Sistema
participant ":User" as UserObj

Usuario -> Sistema : iniciarSesion(email, password)
Sistema -> UserObj : buscarPorEmail(email)
UserObj --> Sistema : usuario
Sistema -> UserObj : verificarCredenciales(password)
UserObj --> Sistema : credencialesValidas

alt credenciales válidas
    Sistema --> Usuario : sesión iniciada
else credenciales inválidas
    Sistema --> Usuario : error de autenticación
end
@enduml
```

### 2.2 Registrar solicitud (crear ticket)

```plantuml
@startuml SecuenciaRegistrarTicket
actor Solicitante
participant "Sistema HelpDesk" as Sistema
participant ":Ticket" as TicketObj
participant ":History" as HistoryObj
participant ":Notification" as NotifObj

Solicitante -> Sistema : registrarSolicitud(titulo, descripcion, categoria, prioridad)
Sistema -> TicketObj : new Ticket(datos, requester=Solicitante)
TicketObj --> Sistema : ticket creado (status=Open)
Sistema -> HistoryObj : new History(ticket, "Creado")
Sistema -> NotifObj : new Notification(destinatario=Supervisor, tipo="NuevoTicket")
Sistema --> Solicitante : confirmación (numero de ticket)
@enduml
```

### 2.3 Asignar ticket

```plantuml
@startuml SecuenciaAsignarTicket
actor Supervisor
participant "Sistema HelpDesk" as Sistema
participant ":Ticket" as TicketObj
participant ":History" as HistoryObj
participant ":Notification" as NotifObj
actor Tecnico

Supervisor -> Sistema : asignarTicket(ticketId, tecnico)
Sistema -> TicketObj : asignar(tecnico)
TicketObj -> TicketObj : status = "In Progress"
TicketObj -> HistoryObj : new History(ticket, "Asignado a " + tecnico)
Sistema -> NotifObj : new Notification(destinatario=Tecnico, tipo="TicketAsignado")
NotifObj --> Tecnico : notifica asignación
Sistema --> Supervisor : confirmación de asignación
@enduml
```

### 2.4 Resolver y cerrar ticket

```plantuml
@startuml SecuenciaCerrarTicket
actor Tecnico
participant "Sistema HelpDesk" as Sistema
participant ":Ticket" as TicketObj
participant ":Comment" as CommentObj
participant ":History" as HistoryObj
participant ":Notification" as NotifObj
actor Solicitante

Tecnico -> Sistema : agregarComentario(ticketId, texto)
Sistema -> TicketObj : agregarComentario(Tecnico, texto)
TicketObj -> CommentObj : new Comment(autor=Tecnico, body=texto)

Tecnico -> Sistema : cambiarEstado(ticketId, "Resolved")
Sistema -> TicketObj : cambiarEstado("Resolved")
TicketObj -> HistoryObj : new History(ticket, "Resuelto")

Tecnico -> Sistema : cerrarTicket(ticketId)
Sistema -> TicketObj : cerrar()
TicketObj -> TicketObj : status = "Closed"
TicketObj -> HistoryObj : new History(ticket, "Cerrado")
Sistema -> NotifObj : new Notification(destinatario=Solicitante, tipo="TicketCerrado")
NotifObj --> Solicitante : notifica cierre
Sistema --> Tecnico : confirmación
@enduml
```

## 3. Casos de uso por módulo

Los cuatro actores especializan a `Usuario` (generalización de actor — mismo criterio de herencia conceptual que semana 4).

### 3.1 Autenticación y usuarios

```plantuml
@startuml CasosUso_AutenticacionUsuarios
left to right direction
actor Usuario
actor Solicitante
actor Tecnico
actor Supervisor
actor Administrador

Usuario <|-- Solicitante
Usuario <|-- Tecnico
Usuario <|-- Supervisor
Usuario <|-- Administrador

rectangle "Módulo: Autenticación y Usuarios" {
  usecase "Iniciar sesión" as UC1
  usecase "Consultar mi perfil" as UC2
  usecase "Listar usuarios" as UC3
  usecase "Consultar catálogos" as UC4
}

Usuario --> UC1
Usuario --> UC2
Usuario --> UC4
Administrador --> UC3
@enduml
```

### 3.2 Gestión de tickets

```plantuml
@startuml CasosUso_GestionTickets
left to right direction
actor Solicitante
actor Tecnico
actor Supervisor

rectangle "Módulo: Gestión de Tickets" {
  usecase "Registrar solicitud" as UC1
  usecase "Consultar tickets" as UC2
  usecase "Consultar detalle de ticket" as UC3
  usecase "Consultar historial de ticket" as UC4
  usecase "Comentar ticket" as UC5
  usecase "Actualizar ticket" as UC6
  usecase "Asignar ticket" as UC7
  usecase "Cambiar estado de ticket" as UC8
  usecase "Cancelar ticket" as UC9
  usecase "Cerrar ticket" as UC10
  usecase "Consultar panel (dashboard)" as UC11
}

Solicitante --> UC1
Solicitante --> UC2
Solicitante --> UC3
Solicitante --> UC4
Solicitante --> UC5

Tecnico --> UC2
Tecnico --> UC3
Tecnico --> UC4
Tecnico --> UC5
Tecnico --> UC8
Tecnico --> UC10

Supervisor --> UC6
Supervisor --> UC7
Supervisor --> UC9
Supervisor --> UC11

UC7 ..> UC4 : <<include>>
UC10 ..> UC4 : <<include>>
@enduml
```

### 3.3 Base de conocimiento

```plantuml
@startuml CasosUso_BaseConocimiento
left to right direction
actor Usuario
actor Tecnico
actor Administrador

rectangle "Módulo: Base de Conocimiento" {
  usecase "Consultar artículos" as UC1
  usecase "Consultar artículo" as UC2
  usecase "Publicar artículo" as UC3
  usecase "Actualizar artículo" as UC4
  usecase "Eliminar artículo" as UC5
}

Usuario --> UC1
Usuario --> UC2
Tecnico --> UC3
Tecnico --> UC4
Administrador --> UC5
@enduml
```

### 3.4 Notificaciones

```plantuml
@startuml CasosUso_Notificaciones
left to right direction
actor Usuario

rectangle "Módulo: Notificaciones" {
  usecase "Consultar notificaciones" as UC1
  usecase "Consultar notificaciones no leídas" as UC2
  usecase "Marcar notificación como leída" as UC3
}

Usuario --> UC1
Usuario --> UC2
Usuario --> UC3
@enduml
```
