"""Cuadernillo IV - Ejercicio 6: FastAPI mínimo: una ruta y un schema."""

from fastapi import FastAPI
from pydantic import BaseModel


class TicketOut(BaseModel):
    id: int
    titulo: str
    prioridad: str


app = FastAPI()

TICKETS_DEMO = [
    {"id": 1, "titulo": "No enciende", "prioridad": "ALTA"},
    {"id": 2, "titulo": "Sin internet", "prioridad": "MEDIA"},
]


@app.get("/tickets", response_model=list[TicketOut])
def listar_tickets() -> list[dict]:
    return TICKETS_DEMO


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
