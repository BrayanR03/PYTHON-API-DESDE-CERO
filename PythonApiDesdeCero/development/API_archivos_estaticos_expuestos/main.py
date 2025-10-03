from fastapi import FastAPI ## ⬅️ Importamos librería FastAPI
from routers import clientes ## ⬅️ Importamos archivo clientes dentro de carpeta routers.
from fastapi.staticfiles import StaticFiles ## ⬅️ Librería que permite exponer los archivos estáticos a internet.
app = FastAPI() ## ⬅️ Instanciamos contexto FastAPI()

app.include_router(router=clientes.router_clientes) ## ⬅️ Instanciamos el router del archivo API independiente.

app.mount(path="/static",app=StaticFiles(directory="static"),name="static")

@app.get("/")
async def main():
    return {"message":"Hola desde FastAPI!!!"}


## ✅ LEVANTAR ESTA API ➡️ uvicorn main:app --reload

## 💡 Tener en cuenta en que carpeta se encuentra ubicado este archivo
##    para poder levantar la API.