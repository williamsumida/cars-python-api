from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from cars_python_api import crud
from cars_python_api.models import CarroRequest
from cars_python_api.database import setup_database, get_database


setup_database()
app = FastAPI()


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
