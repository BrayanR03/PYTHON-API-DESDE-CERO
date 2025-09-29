from fastapi import FastAPI ## ⬅️ Importamos librería FastAPI
from fastapi import status ## ⬅️ Importamos librería para el status 
from fastapi import HTTPException ## ⬅️ Importamos librería para el manejo correcto de errores en los endpoints
from pydantic import BaseModel ## ⬅️ Importamos librería para el formato adecuado de datos

app = FastAPI() ## Establecemos el contexto de FastAPI

## A través de una clase en Python enviámos BaseModel
## para el formato adecuado del envío y recepción de datos a través de la red.
class Cliente(BaseModel):
    id : int
    nombre : str
    apellido : str
    edad : int
    

## Base de Datos simulada como una lista de objetos de la clase Cliente.
clientes_bd = [
    Cliente(id=1,nombre="Pepito",apellido="Perez",edad=25),
    Cliente(id=2,nombre="Juanito",apellido="Mendez",edad=30),
    Cliente(id=3,nombre="Pedrito",apellido="Rojas",edad=18),
]


def buscar_cliente(id:int):
    try:
        return [i for i in clientes_bd if i.id==id][0]
    except:
        return {"message":"El cliente no existe"}
## 💡 buscar_cliente) Al ser una función auxiliar, no es necesario utilizar HTTPException para manejar su lógica.
    

## Petición GET que permite RETORNAR toda la información de la base de datos simulada ✅
@app.get("/",status_code=status.HTTP_200_OK)
async def listar_clientes():
    return clientes_bd

## Petición POST que permite REGISTRAR información de un producto ✅
@app.post("/cliente",status_code=status.HTTP_201_CREATED)
async def registrar_cliente(cliente:Cliente):
    if type(buscar_cliente(cliente.id))==Cliente:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="El cliente a registrar existe!!!")
    else:
        clientes_bd.append(cliente)
        return {"message":"El cliente se registró correctamente!"}    


## Petición PUT que permite ACTUALIZAR información de un producto ✅          
@app.put("/cliente",status_code=status.HTTP_201_CREATED)
async def actualizar_cliente(cliente:Cliente):
    if type(buscar_cliente(cliente.id)) == Cliente:
        for i,j in enumerate(clientes_bd):
            if j.id==cliente.id:
                clientes_bd[i] = cliente
        return {"message":"Se actualizó el cliente!!!"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="El cliente no existe")


## Petición DELETE que permite ELIMINAR un producto ✅
@app.delete("/cliente/{id}",status_code=status.HTTP_200_OK)
async def eliminar_cliente(id:int):
    if type(buscar_cliente(id))==Cliente:
        for _,j in enumerate(clientes_bd):
            if j.id==id:
                clientes_bd.remove(j)
        return{"message":"Se eliminó el cliente"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="El cliente no existe!!")
    

## ✅ LEVANTAR ESTA API ➡️ uvicorn clientes:app --reload

## 💡 Tener en cuenta en que carpeta se encuentra ubicado este archivo
##    para poder levantar la API.