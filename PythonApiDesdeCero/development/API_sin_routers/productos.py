from fastapi import FastAPI ## ⬅️ Importamos librería FastAPI
from fastapi import status ## ⬅️ Importamos librería para el status 
from fastapi import HTTPException ## ⬅️ Importamos librería para el manejo correcto de errores en los endpoints
from pydantic import BaseModel ## ⬅️ Importamos librería para el formato adecuado de datos

app = FastAPI() ## Establecemos el contexto de FastAPI

## A través de una clase en Python enviámos BaseModel
## para el formato adecuado del envío y recepción de datos a través de la red.
class Producto(BaseModel):
    id : int
    descripcion : str
    stock : int
    precio : float
    

## Base de Datos simulada como una lista de objetos de la clase Producto.
productos_bd = [
    Producto(id=1,descripcion="PRODUCTO A",stock=120,precio=12.24),
    Producto(id=2,descripcion="PRODUCTO B",stock=20,precio=2.24),
    Producto(id=3,descripcion="PRODUCTO C",stock=10,precio=6.25),
    Producto(id=4,descripcion="PRODUCTO D",stock=19,precio=7.50),
    Producto(id=5,descripcion="PRODUCTO E",stock=14,precio=6.30)
]


def buscar_producto(id:int):
    try:
        return [i for i in productos_bd if i.id==id][0]
    except:
        return {"message":"El producto no existe"}
## 💡 buscar_producto() Al ser una función auxiliar, no es necesario utilizar HTTPException para manejar su lógica.
    

## Petición GET que permite RETORNAR toda la información de la base de datos simulada ✅
@app.get("/",status_code=status.HTTP_200_OK)
async def listar_productos():
    return productos_bd

## Petición POST que permite REGISTRAR información de un producto ✅
@app.post("/producto",status_code=status.HTTP_201_CREATED)
async def registrar_producto(producto:Producto):
    if type(buscar_producto(producto.id))==Producto:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="El producto a registrar existe!!!")
    else:
        productos_bd.append(producto)
        return {"message":"El producto se registró correctamente!"}    


## Petición PUT que permite ACTUALIZAR información de un producto ✅          
@app.put("/producto",status_code=status.HTTP_201_CREATED)
async def actualizar_producto(producto:Producto):
    if type(buscar_producto(producto.id)) == Producto:
        for i,j in enumerate(productos_bd):
            if j.id==producto.id:
                productos_bd[i] = producto
        return {"message":"Se actualizó el producto!!!"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="El producto no existe")


## Petición DELETE que permite ELIMINAR un producto ✅
@app.delete("/producto/{id}",status_code=status.HTTP_200_OK)
async def eliminar_producto(id:int):
    if type(buscar_producto(id))==Producto:
        for _,j in enumerate(productos_bd):
            if j.id==id:
                productos_bd.remove(j)
        return{"message":"Se eliminó el producto"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="El producto no existe!!")
    

## ✅ LEVANTAR ESTA API ➡️ uvicorn productos:app --reload

## 💡 Tener en cuenta en que carpeta se encuentra ubicado este archivo
##    para poder levantar la API.