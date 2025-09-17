from fastapi import FastAPI ## Librería FastAPI

app = FastAPI() ## Contexto de FastAPI

##===================================================================================================

## 1️⃣ PETICIÓN HTTP: ** GET APUNTANDO A RUTA INICIAL ("/") **
@app.get("/")
async def peticion_get():
    return {"message_get":"Hola desde la petición get!!!"}

## ✅ Podemos verificar el retorno de la petición get a través de: http://localhost:8000/
## ✅ Verificar imagen: output_peticion_http_get.png

##===================================================================================================

## 2️⃣ PETICIÓN HTTP: ** POST APUNTANDO A RUTA ("/pruebita/post") **
@app.post("/pruebita/post") ## 💡 Post permite almacenar información (En el próximo capítulo veremos el funcionamiento de todas las APIs unidas)
async def peticion_post():
    return {"message_get":"Hola desde la petición post!!!"}

## ✅ Podemos verificar el retorno de la petición get a través de: http://localhost:8000/
## ✅ Verificar imagen: output_peticion_http_post.png

##===================================================================================================

## 3️⃣ PETICIÓN HTTP: ** PUT APUNTANDO A RUTA ("/pruebita/put") **
@app.put("/pruebita/put") ## 💡 Post permite modificar información (En el próximo capítulo veremos el funcionamiento de todas las APIs unidas)
async def peticion_put():
    return {"message_get":"Hola desde la petición put!!!"}

## ✅ Podemos verificar el retorno de la petición get a través de: http://localhost:8000/
## ✅ Verificar imagen: output_peticion_http_put.png

##===================================================================================================

## 4️⃣ PETICIÓN HTTP: ** DELETE APUNTANDO A RUTA ("/pruebita/delete") **
@app.delete("/pruebita/delete") ## 💡 Post permite modificar información (En el próximo capítulo veremos el funcionamiento de todas las APIs unidas)
async def peticion_delete():
    return {"message_get":"Hola desde la petición delete!!!"}

## ✅ Podemos verificar el retorno de la petición get a través de: http://localhost:8000/
## ✅ Verificar imagen: output_peticion_http_delete.png

"""
    💡 En este archivo solo estamos definiendo los endpoint, sin nada de lógica (por el momento).
        En el siguiente capítulo veremos como establecemos lógica entre cada endpoint.
"""
"""
    💡 Se realizaron las pruebas de las peticiones POST, PUT Y DELETE en Postmam el cuál
        permite interactuar con los endpoint de una API en el caso del envío de datos a través
        de la red mediante HTTP. 
"""
## ✅ LEVANTAR ESTA API ➡️ uvicorn peticiones_http:app --reload