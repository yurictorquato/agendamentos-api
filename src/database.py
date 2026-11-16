from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool


def make_engine(url: str) -> Engine:
    if url in ("sqlite://", "sqlite:///:memory:"):
        return create_engine(
            url,
            connect_args={"check_same_thread": False},
            poolclass=StaticPool,
        )

    return create_engine(
        url,
        connect_args={"check_same_thread": False},
    )


engine = make_engine("sqlite:///./agendamentos.db")


def get_session():
    with Session(engine) as session:
        yield session
