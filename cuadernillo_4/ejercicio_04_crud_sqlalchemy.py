"""Cuadernillo IV - Ejercicio 4: CRUD real con SQLAlchemy."""

from sqlalchemy import ForeignKey, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


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


def main() -> None:
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        usuario = Usuario(nombre="Ana Lopez", correo="ana@umg.edu.gt")
        session.add(usuario)
        session.commit()

        ticket = Ticket(titulo="No enciende", prioridad="ALTA", solicitante_id=usuario.id)
        session.add(ticket)
        session.commit()

        resultado = session.scalars(select(Ticket)).all()
        for t in resultado:
            print(t.id, t.titulo, t.prioridad)


if __name__ == "__main__":
    main()
