from pydantic import BaseModel
from datetime import date

from cars_python_api.database import Base


class CarroRequest(BaseModel):
    nome: str
    km_por_galao: float
    cilindros: float
    cavalos_de_forca: float
    peso: float
    aceleracao: float
    ano: date
    origem: str


class MarcaRequest(BaseModel):
    nome: str
    origem: str
