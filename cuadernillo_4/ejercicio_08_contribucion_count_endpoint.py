"""Cuadernillo IV - Ejercicio 8: Primera contribución real: GET /api/tickets/count."""

# --- Agregar en app/services/tickets.py, dentro de class TicketService ---

def count(self, user: User) -> dict:
    requester_id = user.id if user.role == "requester" else None
    return {"count": len(self.tickets.list(requester_id=requester_id))}


# --- Agregar en app/api/routes/tickets.py, junto a las demas rutas de /api/tickets ---

@router.get("/api/tickets/count")
def count(user: Annotated[User, Depends(current_user)], db: Annotated[Session, Depends(get_db)]) -> dict:
    return TicketService(db).count(user)


# Nota: no importa si esta ruta se declara antes o despues de
# GET /api/tickets/{ticket_id}, porque ticket_id: int usa un conversor de
# ruta que solo matchea digitos -- "count" nunca coincide con ese patron.
# Aun asi, por claridad, conviene declarar las rutas fijas (/count) antes
# que las rutas con parametro ({ticket_id}).
