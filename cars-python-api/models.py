from sqlalchemy import Column, Integer, Numeric, String, Date
from database import Base


class Carro(Base):
    __tablename__ = "carro"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    km_por_galao = Column(Numeric)
    cilindros = Column(Numeric)
    cavalos_de_forca = Column(Numeric)
    peso = Column(Numeric)
    aceleracao = Column(Numeric)
    ano = Column(Date)
    origem = Column(String)


class Marca(Base):
    __tablename__ = "marca"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    origem = Column(String)
