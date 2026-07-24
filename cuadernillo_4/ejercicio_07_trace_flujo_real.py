"""Cuadernillo IV - Ejercicio 7: Leer un flujo real en help_desk_EDU."""

# IMPORTANTE: este script debe ejecutarse desde dentro de help_desk_EDU/
# (para que el paquete "app" se resuelva), por ejemplo:
#   cd help_desk_EDU && python3 trace_listar_tickets.py

from datetime import datetime, timedelta

from app.core.database import create_session_factory  # infraestructura real
from app.models import Ticket, User  # modelos reales (capa Model)
from app.services.tickets import TicketService  # logica real (capa Service, que usa el Repository)

# Paso 1: preparar una base de datos de prueba, igual que hace un test
session_factory = create_session_factory("sqlite://")
db = session_factory()

# Paso 2: crear los datos que normalmente vendrian de un POST /api/auth/register
requester = User(email="ana@umg.edu.gt", name="Ana Lopez", role="requester", password_hash="x")
db.add(requester)
db.commit()

ticket = Ticket(
    title="No enciende",
    description="El equipo no enciende",
    category="Hardware",
    priority="High",
    requester_id=requester.id,
    due_at=datetime.utcnow() + timedelta(hours=24),
)
db.add(ticket)
db.commit()

# Paso 3: esta es EXACTAMENTE la linea que ejecuta la ruta GET /api/tickets
# (ver app/api/routes/tickets.py: TicketService(db).list(user, status_filter, category, priority))
service = TicketService(db)
resultado = service.list(requester, None, None, None)

# TicketService.list() llama a self.tickets.list(...) -- eso es TicketRepository, la capa
# que arma el SELECT contra la base de datos y devuelve objetos Ticket.
print(resultado)
