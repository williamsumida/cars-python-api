from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from cars_python_api import crud
from cars_python_api.models import CarroRequest, MarcaRequest
from cars_python_api.database import setup_database, get_database


setup_database()
app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/carro")
def create_carro(carro_request: CarroRequest, db: Session = Depends(get_database)):
    """Cria um carro no banco de dados"""
    crud.create_carro(carro_request, db)
    return {"code": "success", "message": "Carro criado com sucesso"}


@app.get("/carro/{carro_id}")
def get_carro(carro_id: int, db: Session = Depends(get_database)):
    carro = crud.get_carro(carro_id, db)

    if carro is None:
        raise HTTPException(status_code=404, detail="Carro não encontrado")

    return carro


@app.get("/carro")
def get_carros(nome: str = "", origem: str = "", db: Session = Depends(get_database)):
    carros = crud.get_carros(nome, origem, db)
    return carros


@app.put("/carro/{carro_id}")
def update_carro(
    carro_id: int, carro_request: CarroRequest, db: Session = Depends(get_database)
):
    carro = crud.get_carro(carro_id, db)

    if not carro:
        raise HTTPException(status_code=404, detail="Carro não encontrado")

    crud.update_carro(carro_id, carro_request, db)
    return {"code": "success", "message": "Carro atualizado com sucesso"}


@app.delete("/carro/{carro_id}")
def delete_carro(carro_id: int, db: Session = Depends(get_database)):
    carro = crud.get_carro(carro_id, db)

    if not carro:
        raise HTTPException(status_code=404, detail="Carro não encontrado")

    crud.delete_carro(carro_id, db)
    return {"code": "success", "message": "Carro deletado com sucesso"}


@app.post("/marca")
def create_marca(marca_request: MarcaRequest, db: Session = Depends(get_database)):
    """Cria um marca no banco de dados"""
    crud.create_marca(marca_request, db)
    return {"code": "success", "message": "Marca criada com sucesso"}


@app.get("/marca/{marca_id}")
def get_marca(marca_id: int, db: Session = Depends(get_database)):
    marca = crud.get_marca(marca_id, db)

    if marca is None:
        raise HTTPException(status_code=404, detail="Marca não encontrada")

    return marca


@app.get("/marca")
def get_marcas(nome: str = "", origem: str = "", db: Session = Depends(get_database)):
    marcas = crud.get_marcas(nome, origem, db)
    return marcas


@app.put("/marca/{marca_id}")
def update_marca(
    marca_id: int, marca_request: MarcaRequest, db: Session = Depends(get_database)
):
    marca = crud.get_marca(marca_id, db)

    if not marca:
        raise HTTPException(status_code=404, detail="Marca não encontrada")

    crud.update_marca(marca_id, marca_request, db)
    return {"code": "success", "message": "Marca atualizada com sucesso"}


@app.delete("/marca/{marca_id}")
def delete_marca(marca_id: int, db: Session = Depends(get_database)):
    marca = crud.get_marca(marca_id, db)

    if not marca:
        raise HTTPException(status_code=404, detail="Marca não encontrada")

    crud.delete_marca(marca_id, db)
    return {"code": "success", "message": "Marca deletada com sucesso"}
