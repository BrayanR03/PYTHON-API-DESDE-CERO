from fastapi import FastAPI ## ⬅️ Importamos librería FastAPI
from pydantic import BaseModel ## ⬅️ Importamos librería para el formato adecuado de datos
from fastapi import HTTPException
from fastapi import status

app = FastAPI() ## Establecemos el contexto de FastAPI

## A través de una clase en Python enviámos BaseModel
## para el formato adecuado del envío y recepción de datos a través de la red.
class Producto(BaseModel):
    id:int
    descripcion:str
    stock:int
    precio: float

## Base de Datos simulada como una lista de objetos de la clase Producto.
productos_bd = [
    
    Producto(id=1,descripcion="Producto A",stock=120,precio=12.50),
    Producto(id=2,descripcion="Producto B",stock=65,precio=10.50),
    Producto(id=3,descripcion="Producto C",stock=30,precio=2.50),
    Producto(id=4,descripcion="Producto D",stock=20,precio=5.50),
    Producto(id=5,descripcion="Producto E",stock=10,precio=78.50)
]

def buscar_producto_bd(id:int):
    try:
        return [i for i in productos_bd if i.id==id][0]
    except:
        # raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail="No existe este producto!!")
        return {"message":"error"} 
## 💡 buscar_producto_bd() Al ser una función auxiliar, no es necesario utilizar HTTPException para manejar su lógica.
    
    
## Petición GET que permite RETORNAR toda la información de la base de datos simulada ✅
@app.get("/",status_code=200)
async def listar_productos():
    return productos_bd


## Petición POST que permite REGISTRAR información de un producto ✅
@app.post("/producto",status_code=201) ## ⬅️ DEFINIMOS UN STATUS CODE DE 200 SIEMPRE QUE LA LLAMADA / OPERACIÓN REALIZADA AL ENDPOINT SEA CORRECTA.
async def registrar_producto(producto:Producto):
    if type(buscar_producto_bd(producto.id))==Producto:
        ## return {"message":"El producto existe!!!"} ## ⬅️ Mensaje de respuesta de error utilizado con anterioridad.
        raise HTTPException(status_code=status.HTTP_200_OK,detail="El producto a registrar, ya existe!!")
    else:
        productos_bd.append(producto)
        return {"message":"Se registró el producto!!"} ## ⬅️ Acá no establecemos un HTTPException porque
                                                       ##    la respuesta del endpoint es correcta y toma por defecto
                                                       ##    el status code definido en la ruta del enpoint.


## Petición PUT que permite ACTUALIZAR información de un producto ✅        
@app.put("/producto",status_code=status.HTTP_200_OK)
async def actualizar_producto(producto:Producto):
    if type(buscar_producto_bd(producto.id))==Producto:
        for i,j in enumerate(productos_bd):
            if j.id ==producto.id:
                productos_bd[i] = producto                
        return {"message":"Se actualizó el producto!!!"}
    else:
        ## return {"message":"El producto no existe"} ## ⬅️ Mensaje de respuesta de error utilizado con anterioridad.
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,detail="El producto a registrar no existe!!")


## Petición DELETE que permite ELIMINAR un producto ✅        
@app.delete("/{id}",status_code=status.HTTP_200_OK)
async def eliminar_producto(id:int):
    if type(buscar_producto_bd(id))==Producto:
        # productos_bd.remove(id)
        for _,j in enumerate(productos_bd):
            if j.id==id:
                productos_bd.remove(j)
        return {"message":"El producto fue eliminado correctamente!!"}
    else:
        ## return {"message":"No existe el producto a eliminar"} ## ⬅️ Mensaje de respuesta de error utilizado con anterioridad.
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="El producto a eliminar no existe!!")

## ✅ LEVANTAR ESTA API ➡️ uvicorn peticiones_http_simulador:app --reload
