
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensagem": "API do Laboratorio 9 funcionando!"}

@app.get("/health")
def verificar_saude():
    return {"status": "ok"}
