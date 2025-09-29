
from fastapi import FastAPI,status

app = FastAPI()


@app.get("/",status_code=status.HTTP_200_OK)
async def main():
    return {"message":"Bienvenido al Archivo Principal de la API"}


## ✅ LEVANTAR ESTA API ➡️ uvicorn main:app --reload

## 💡 Tener en cuenta en que carpeta se encuentra ubicado este archivo
##    para poder levantar la API.