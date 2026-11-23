
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensagem": "API funcionando no ambiente de homologacao!"}

@app.get("/health")
def verificar_saude():
    return {"status": "ok"}


