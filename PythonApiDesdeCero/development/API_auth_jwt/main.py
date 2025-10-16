from fastapi import FastAPI ## ⬅️ Importamos librería FastAPI
from routers import usuarios ## ⬅️ Importamos archivo usuarios dentro de carpeta routers.

app = FastAPI() ## ⬅️ Instanciamos contexto FastAPI()

app.include_router(router=usuarios.router_usuarios) ## ⬅️ Instanciamos el router del archivo API independiente.

@app.get("/")
async def main():
    return {"message":"Hola desde FastAPI!!!"}


## ✅ LEVANTAR ESTA API ➡️ uvicorn main:app --reload
"""
    Al instanciar los routers de los archivos que antes funcionaban como APIs independientes, 
    podemos centralizar su uso en main.py. Gracias a los prefijos definidos para cada router,
    basta con levantar un único archivo principal para acceder a todos los recursos de manera
    organizada y modular.
"""

## 💡 Tener en cuenta en que carpeta se encuentra ubicado este archivo
##    para poder levantar la API.