# 📌 CAPÍTULO 07. HTTP STATUS CODE 📢

En este capítulo exploraremos uno de los **conceptos fundamentales en redes** y su relación con FastAPI:  
los **códigos de estado HTTP (Status Codes)**.

Aunque pueda parecer algo simple, **toda la comunicación en Internet se basa en estos códigos**:  
cada vez que accedemos a una página, realizamos una petición a una API o enviamos datos, el servidor responde con un **status code** que indica el resultado de la operación.

Estos códigos permiten:
- Informar si una operación se ejecutó correctamente.
- Notificar errores de validación o de servidor.
- Mantener el control de los endpoints para evitar que el sistema/API se bloquee o colapse.

👉 La documentación oficial de FastAPI ofrece una lista completa:  
[FastAPI Status Codes](https://fastapi.tiangolo.com/reference/status/?h=status#fastapi.status.WS_1015_TLS_HANDSHAKE)

---

## 🔑 Status Codes más utilizados en APIs

A continuación, los códigos más comunes en el desarrollo de APIs:

- **200** → Operación exitosa.  
- **201** → Recurso creado (ideal para peticiones **POST**).  
- **204** → Sin contenido (útil para validar existencia de un objeto sin devolver datos).  
- **400** → Error en la solicitud del cliente.  
- **404** → Recurso no encontrado.  
- **500** → Error interno del servidor.

FastAPI permite **definir el código de estado** en cada endpoint utilizando el parámetro `status_code`  
y el módulo `status` para mayor legibilidad.

---

## 🛠️ Definiendo Status Codes en un Endpoint

Podemos establecer el código de respuesta directamente en el decorador del endpoint.

**Sintaxis básica:**
```python
@contexto_fastapi.peticion_http(status_code=CódigoStatusCode)
async def nombre_funcion():
    return logica
```
**Ejemplo 1**:
```python
@app.get("/",status_code=200)
async def listar_productos():
    return productos_bd
```
**Ejemplo 2** Usando el módulo `status`:
```python
from fastapi import status

@app.get("/", status_code=status.HTTP_200_OK)
async def listar_productos():
    return productos_bd
```
💡 Si no especificamos un status_code, FastAPI devolverá 200 OK por defecto.


Podemos incluso forzar un código distinto, aunque no sea un error real:
```python
@app.get("/", status_code=404)  # Fuerza la respuesta 404
async def listar_productos():
    return productos_bd
```
⚠️ Sin embargo, devolver un 404 sin motivo confundiría al consumidor de la API.

---
## 🚨 Personalización de errores con HTTPException

FastAPI nos permite **interrumpir el flujo de un endpoint** y enviar un código de estado personalizado cuando ocurre una excepción, utilizando `HTTPException` junto con `raise`.

**Sintaxis**:
```python
from fastapi import HTTPException, status

@contexto_fastapi.peticion_http()
async def nombre_funcion():
    if condicion_de_error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Mensaje de error personalizado."
        )
    return {"message": "Operación exitosa"}
```
💡 HTTPException debe usarse dentro del endpoint, porque su propósito es finalizar la petición inmediatamente.
En funciones auxiliares, en cambio, se utilizan return normales para mantener el flujo interno.

### 🧩 Ejemplo práctico

Petición POST para registrar un producto:

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

class Producto(BaseModel):
    id: int
    nombre: str

productos_bd = []

@app.post("/producto", status_code=201)
async def registrar_producto(producto: Producto):
    if any(p.id == producto.id for p in productos_bd):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El producto ya existe en la base de datos."
        )
    productos_bd.append(producto)
    return {"message": "Producto registrado con éxito"}
```
En este ejemplo:

* Si el producto ya existe, lanzamos un HTTP 400 con un mensaje personalizado.

* Si la operación es correcta, retornamos un 201 Created.

### ✅ Recomendaciones

* Usa status codes que reflejen el resultado real de la operación.

* Emplea HTTPException para interrumpir el flujo de forma controlada.

* Mantén coherencia: no devuelvas un 404 si la operación fue exitosa.


Para más detalle, revisar el archivo [peticiones_con_status_code.py](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/development/peticiones_con_status_code.py) y su diferencia con el
[archivo peticiones_sin_status_code.py](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/development/peticiones_sin_status_code.py)


---
### 📖 Siguiente paso → [08_routers.md](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/documentation/08_routers.md)  
#### En el siguiente archivo aprenderás sobre los `routers` y como jerarquizar tu API.
---
# Sobre el autor  

Gracias por leer este séptimo capítulo 🔥.  

🔗 Conéctate conmigo en mis redes y sigue de cerca mi contenido:  
- [LinkedIn](https://www.linkedin.com/in/brayan-rafael-neciosup-bola%C3%B1os-407a59246/)  
- [GitHub](https://github.com/BrayanR03)  
- [Portafolio Web](https://bryanneciosup626.wixsite.com/brayandataanalitics)  


Nos vemos en el próximo archivo 👊🚀  
