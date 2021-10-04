from sqlalchemy.orm import Session

from cars_python_api.models import CarroRequest, MarcaRequest
from cars_python_api.database_models import Carro, Marca


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


def create_marca(marca_request: MarcaRequest, db: Session):
    marca = Marca()
    marca.nome = marca_request.nome
    marca.origem = marca_request.origem
    marca.is_active = True

    db.add(marca)
    db.commit()


def get_marca(marca_id: int, db: Session):
    return db.query(Marca).filter(Marca.id == marca_id, Marca.is_active == True).first()


def get_marcas(nome: str, origem: str, db: Session):
    nome_filter = Marca.nome.contains(nome)
    origem_filter = Marca.origem == origem
    is_active_filter = Marca.is_active == True

    if origem:
        marcas = (
            db.query(Marca).filter(nome_filter, origem_filter, is_active_filter).all()
        )
    else:
        marcas = db.query(Marca).filter(nome_filter, is_active_filter).all()

    return marcas


def update_marca(marca_id: int, marca_request: MarcaRequest, db: Session):
    db.query(Marca).filter(Marca.id == marca_id).update(
        {
            Marca.nome: marca_request.nome,
            Marca.origem: marca_request.origem,
        },
        synchronize_session="fetch",
    )
    db.commit()


def delete_marca(marca_id: int, db: Session):
    db.query(Marca).filter(Marca.id == marca_id).update({Marca.is_active: False})
    db.commit()
