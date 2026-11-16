from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass


class Base(MappedAsDataclass, DeclarativeBase):
    pass


class Client(Base):
    __tablename__ = "clients"

    


class Professional(Base):
    __tablename__ = "professionals"

    ...


class Service(Base):
    __tablename__ = "services"

    ...
