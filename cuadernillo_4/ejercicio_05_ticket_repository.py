"""Cuadernillo IV - Ejercicio 5: GestorTickets → TicketRepository."""

from sqlalchemy import ForeignKey, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    pass


class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))


class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(160))
    solicitante_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))


class TicketRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def by_id(self, ticket_id: int) -> Ticket | None:
        return self.db.get(Ticket, ticket_id)

    def list(self) -> list[Ticket]:
        return list(self.db.scalars(select(Ticket)).all())

    def add(self, ticket: Ticket) -> Ticket:
        self.db.add(ticket)
        self.db.commit()
        self.db.refresh(ticket)
        return ticket


def main() -> None:
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        usuario = Usuario(nombre="Ana Lopez")
        session.add(usuario)
        session.commit()

        repository = TicketRepository(session)
        ticket = repository.add(Ticket(titulo="No enciende", solicitante_id=usuario.id))

        encontrado = repository.by_id(ticket.id)
        print(encontrado.titulo)
        print(repository.list())


if __name__ == "__main__":
    main()
