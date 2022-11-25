from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{id}")
def read(id: int, nome: Union[str, None] = None):
    return {"item_id": id, "nome": nome}

@app.post("/post/")
def post():
    return {"post": "Enviar"}

@app.put("/put/")
def put():
    return {"put": "Colocar"}

@app.delete("/delete/")
def delete():
    return {"delete": "Excluir"}