"""Cuadernillo IV - Ejercicio 3: Convertir Ticket en un modelo SQLAlchemy real."""

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    correo: Mapped[str] = mapped_column(String(120))


class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(160))
    prioridad: Mapped[str] = mapped_column(String(30))
    solicitante_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))


if __name__ == "__main__":
    print(Ticket.__tablename__, [c.name for c in Ticket.__table__.columns])
