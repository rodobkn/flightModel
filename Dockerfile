FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install -r requirements_prod.txt

CMD uvicorn challenge.api:app --port=8080 --host=0.0.0.0
