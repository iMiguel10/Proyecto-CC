from base import Base
from sqlalchemy import Column, String, Integer, Numeric


class Entradas(Base):
    __tablename__ = 'entradas'

    id = Column(Integer, primary_key=True)
    evento = Column(String)
    precio = Column(Numeric)
    propietario = Column(String)
    descripcion = Column(String)

    def __init__(self, evento, precio, propietario,descripcion):
        self.evento = evento
        self.precio = precio
        self.propietario = propietario
        self.descripcion = descripcion

    def __repr__(self):
        return '<id {}>'.format(self.id)
