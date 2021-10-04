from sqlalchemy.orm import Session

from cars_python_api.models import CarroRequest
from cars_python_api.database_models import Carro


def create_carro(carro_request: CarroRequest, db: Session):
    carro = Carro()
    carro.nome = carro_request.nome
    carro.km_por_galao = carro_request.km_por_galao
    carro.cilindros = carro_request.cilindros
    carro.cavalos_de_forca = carro_request.cavalos_de_forca
    carro.peso = carro_request.peso
    carro.aceleracao = carro_request.aceleracao
    carro.ano = carro_request.ano
    carro.origem = carro_request.origem
    carro.is_active = True

    db.add(carro)
    db.commit()


def get_carro(carro_id: int, db: Session):
    return db.query(Carro).filter(Carro.id == carro_id, Carro.is_active == True).first()


def get_carros(nome: str, origem: str, db: Session):
    nome_filter = Carro.nome.contains(nome)
    origem_filter = Carro.origem == origem
    is_active_filter = Carro.is_active == True

    if origem:
        carros = (
            db.query(Carro).filter(nome_filter, origem_filter, is_active_filter).all()
        )
    else:
        carros = db.query(Carro).filter(nome_filter, is_active_filter).all()

    return carros


def update_carro(carro_id: int, carro_request: CarroRequest, db: Session):
    db.query(Carro).filter(Carro.id == carro_id).update(
        {
            Carro.nome: carro_request.nome,
            Carro.km_por_galao: carro_request.km_por_galao,
            Carro.cilindros: carro_request.cilindros,
            Carro.cavalos_de_forca: carro_request.cavalos_de_forca,
            Carro.peso: carro_request.peso,
            Carro.aceleracao: carro_request.aceleracao,
            Carro.ano: carro_request.ano,
            Carro.origem: carro_request.origem,
        },
        synchronize_session="fetch",
    )
    db.commit()


def delete_carro(carro_id: int, db: Session):
    db.query(Carro).filter(Carro.id == carro_id).update({Carro.is_active: False})
    db.commit()
