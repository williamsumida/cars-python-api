FROM python:3.8.10-slim

COPY ./cars_python_api /app/cars_python_api
COPY ./requirements.txt /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "cars_python_api.app:app", "--host=0.0.0.0", "--reload"]
