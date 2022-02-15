# Ricardo Amoedo
# version: 1.0

# bibliotecas
from fastapi import FastAPI

# instanciando o fastapi
app = FastAPI()


# rota raiz
@app.get("/")
async def raiz():
    return {"status": 200, "Message": "ok"}


