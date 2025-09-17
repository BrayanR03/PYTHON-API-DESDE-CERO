from fastapi import FastAPI ## Importamos librería FastAPI
from pydantic import BaseModel
app = FastAPI() ## Establecemos el contexto de FastAPI

## 💡 Base de Datos simulada mediante diccionario de pyhon:
productos = [
    {"ProductoID":1,"Descripcion":"Producto A","Stock":120,"Precio":25.00},
    {"ProductoID":2,"Descripcion":"Producto B","Stock":20,"Precio":50.00},
    {"ProductoID":3,"Descripcion":"Producto C","Stock":10,"Precio":75.00},
    {"ProductoID":4,"Descripcion":"Producto D","Stock":20,"Precio":100.00}
]


## 💡 Función que permite realizar a búsqueda de un dato mediante un id.
def buscar_producto(id:int):
    return [i for i in productos if i["ProductoID"]==id][0] ## List comprenhension que retorna el valor de la posición 0.

## 💡 Endpoint principal de la API
@app.get("/")
async def main():
    return productos

## ===================================== GET ================================

## 💡 Ednpoint de petición GET
##--- ✅ Envío de datos mediante el PATH (Url del acceso al endpoint)
@app.get("/producto/{id}") ## ➡️ Utilizamos el envío de parámetros con PATH (Para campos obigatorios)
async def peticion_get(id:int):
    return buscar_producto(id)

##--- ✅ Envío de datos mediante QUERYS (Url del acceso mediante http://localhost:8000/producto/?id=1) ⬅️ Usamos POSTMAN
@app.get("/producto/")# ➡️ Utilizamos el envío de parámetros con QUERY (Para campos opcionales y consultas dinámicas)
async def peticion_get(id:int):
    return buscar_producto(id)
    ## 💡 Revisar imagen: ENVIO_DATOS_QUERY_POSTMAN.png
## ==========================================================================


## ===================================== MODIFICACIONES PREVIAS ✍️ ================================ 

## Creamos la clase y mediante BaseModel etstablecemos que será una entidad con un formato
## adecuado para nuestro envío de información a través de la red.

from pydantic import BaseModel

class Producto(BaseModel):
    producto_id : int
    descripcion: str
    stock : int
    precio : float
    
## 💡 Además, debemos modificar nuestra Base de Datos simulada en un diccionario de python:

productos_bd = [
    Producto(producto_id=1,descripcion="Producto A",stock=120,precio=25.00),
    Producto(producto_id=2,descripcion="Producto B",stock=20,precio=50.00),
    Producto(producto_id=3,descripcion="Producto C",stock=10,precio=75.00),
    Producto(producto_id=4,descripcion="Producto D",stock=20,precio=100.00)
]

## 💡 También, debemos modificar la función que permite realizar la búsqueda de un dato mediante un id.
def buscar_producto_bd(id:int):
    try:
        return [i for i in productos_bd if i.producto_id==id][0] ## List comprenhension que retorna el valor de la entidad en la posición 0.
        ## 💡 Recordemos que cada valor iterado es un objeto de la clase Producto y 
        ##    nos permitirá evaluar su existencia mediante su tipo (Producto) [Ver endpoint POST]
    except:
        return {"message":"No existe el producto"}

## 💡 Posterior a ello, debemos modificar el llamado de nuestra petición get
##    que apuntaba a la Base de Datos simulada con un diccionario de Python
##    por la que tenía la entidad Producto en su lista (productos_bd)

## 💡 Endpoint actualizado con el diccionario que simula la Base de Datos de productos.
@app.get("/productosbd")
async def main():
    return productos_bd ## Retorna todos los productos establecidos mediante la entidad Products

## ==========================================================================


## ===================================== POST ================================ 

##--- EN ESTE CASO, ESTE ENDPOINT AL NO TENER ESPECIFICADO UN FORMATO ADECUADO
##--- SALDRÁ ERROR CADA VEZ QUE ENVIEMOS DATOS A TRAVÉS DEL BODY DE LA PETICIÓN HTTP (POST) ❌ 
# @app.post("/producto/")
# async def peticion_post(productoID:int,descripcion:str,stock:int,precio:float): ## ⬅️ Enviamos los parámetros individualizados
#     return productoID

## ✅ Solución
## 💡 Ednpoint de petición POST
@app.post("/producto")
async def peticion_post(producto:Producto): ## ⬅️ Enviamos como parámetro el objeto de la clase Producto (encapsulando todos sus atributos)
    if type(buscar_producto_bd(producto.producto_id))==Producto: ## ⬅️ Validamos la existencia del producto a registrar.
        return {"message":"El producto a registrar ya existe"}
    else:
        productos_bd.append(producto) ## ⬅️ En caso no exista, registramos en la lista el nuevo objeto de Producto.
        return {"message":"Producto Registrado Correctamente"}

    ## 💡 Revisar imagen: ENVIO_DATOS_POST_POSTMAN.png


## ==========================================================================


## ===================================== PUT ================================ 

## 💡 Ednpoint de petición PUT
@app.put("/producto")
async def peticion_put(producto:Producto): ## ⬅️ Enviamos como parámetro el objeto de la clase Producto (encapsulando todos sus atributos)
    producto_buscado = buscar_producto_bd(producto.producto_id) 
    if type(producto_buscado)==Producto: ## ⬅️ Validamos la existencia del producto a actualizar.
        for i,j in enumerate(productos_bd):
             if j==producto_buscado:
                 productos_bd[i]=producto                           
        return {"message":"El producto se actualizó"}
    else:
        return {"message":"El Producto a Actualizar no existe!"}

    ## 💡 Revisar imagen: ENVIO_DATOS_PUT_POSTMAN.png


## ==========================================================================


## ===================================== DELETE ================================ 
##--- ✅ Envío de datos mediante el PATH (Url del acceso al endpoint)
## 💡 Ednpoint de petición DELETE
@app.delete("/producto/{id}") ## ➡️ Utilizamos el envío de parámetros con PATH (Para campos obigatorios)
async def peticion_delete(id:int):
    
    elimino = False  ## ⬅️ Creamos una variable que represente el estado de eliminación del producto.
    for i in productos_bd: ## ⬅️ Iteramos sobre todos los productos de nuestra base de datos simulada.
        if i.producto_id==id: ## ⬅️ Cuando el id enviado por el path del endpoint haga match con el id iterado
            productos_bd.remove(i) ## ⬅️ Removemos todo el objeto de la entidad de nuesra base de datos simulada
        elimino = True ## ⬅️ Modificamos el estado de eliminación el producto.
        
    if elimino: ## ⬅️ En caso sea verdadero, retornamos el siguiente JSON
        return {"message":"Se eliminó el producto!!!"} 
    
    return {"message":"El producto no existe!!"} ## ⬅️ De lo contrario, el id del producto enviado no existe en nuestra base de datos simulada.
        
    ## 💡 Revisar imagen: ENVIO_DATOS_DELETE_POSTMAN.png
## ==========================================================================

## ✅ LEVANTAR ESTA API ➡️ uvicorn peticiones_http_simulador:app --reload