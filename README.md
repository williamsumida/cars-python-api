# API Gerenciamento de Carros com FastAPI

## Rodar o projeto
### Docker
Exemplo para executar a API com o Docker:
```
docker build -t carros:1.0.0 .
docker run -p 8000:8000 --name API-Carros carros:1.0.0
```

### Python 3.8 (uvicorn)
Exemplo para executar a API com Python:
```
pip3 install -r requirements.txt
uvicorn cars_python_api.app:app --reload
```

## Documentação
A documentação da API se encontra na pasta raiz do projeto (documentacao.yaml).

Pode também ser lida ao rodar o projeto e acessar a url http://localhost:8000/docs
