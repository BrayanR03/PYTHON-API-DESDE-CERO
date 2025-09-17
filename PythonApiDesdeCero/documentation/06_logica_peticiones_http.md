# 📌 CAPÍTULO 06. LÓGICA DE PETICIONES HTTP  
## 📝 Trabajando con datos simulados

En este capítulo simularemos una **base de datos** utilizando una simple **lista de diccionarios en Python**, con el objetivo de comprender cómo **leer, almacenar, actualizar y eliminar información** a través de los diferentes métodos HTTP.  

Esto nos permitirá visualizar el **flujo completo de trabajo** de los endpoints y su respectivo protocolo HTTP, antes de conectarnos a una base de datos real.

> 💡 Para realizar las pruebas de envío y recepción de datos, utilizaremos **Postman**, una herramienta que nos permite simular peticiones a nuestra API.

---

## 🔎 Peticiones GET: Envío de datos

En una **petición GET**, podemos realizar búsquedas de información específica.  
Existen **dos formas principales de enviar datos en una petición GET**:

### 1️⃣ Envío de datos mediante **Path Parameters**

Permite enviar datos a través de la URL definida en el endpoint.  
Se utiliza generalmente para **campos obligatorios**.

**Sintaxis básica:**
```python
@app.get("/rutaEspecificar/valorEnviar")
async def funcion_get_path(valorEnviar:tipoDatoValorEnviar):
    return funcion_busqueda_valor(valorEnviar)
```

**Ejemplo:**
```python
@app.get("/producto/{id}") 
async def peticion_get(id:int): ##⬅️ EN ESTE CASO, FASTAPI NECESITARÁ EL TIPADO ESTÁTICO EN SUS PARÁMETROS
    return buscar_producto(id)
```

### 2️⃣ Envío de datos mediante Query Parameters
Permite enviar datos a través de la URL utilizando el formato `?parametro=valor`.
Se emplea, por lo general, para campos opcionales o consultas dinámicas.

**Sintaxis básica:**
```python
@app.get("/rutaEspecificar/")
async def funcion_get_query(valorEnviar:tipoDatoValorEnviar):
    return funcion_busqueda_valor(valorEnviar)
```
```python
@app.get("/producto/") 
async def peticion_get(id:int): #⬅️ EN ESTE CASO, FASTAPI NECESITARÁ EL TIPADO ESTÁTICO EN SUS PARÁMETROS
    return buscar_producto(id)
```
Revisar la imagen ENVIO_DATOS_QUERY_POSTMAN.png para observar cómo se envían parámetros de tipo query en Postman.

---
## 📨 Peticiones POST: Envío de datos en el Body

Para el caso de POST, los datos se envían en el cuerpo de la petición (body), generalmente en formato JSON (JavaScript Object Notation).

En Postman, podemos enviar un diccionario de Python (formato JSON) en la pestaña Body, pero si lo probamos directamente, FastAPI mostrará un error (ver imagen POSTMAN_BODY_ERROR_POST.png).

Este error ocurre porque **FastAPI no reconoce automáticamente el formato de los datos enviados**. Para solucionarlo, utilizamos **Pydantic** y su clase `BaseModel`, que permite validar y formatear los datos entrantes.

Ejemplo:
```python
from pydantic import BaseModel ## Formatea y valida los datos del body     
class nombreClaseEntidad(BaseModel):
  atributo1:tipo_dato
  atributo2:tipo_dato
  atributoN:tipo_dato
  """ Mediante una clase en python, BaseModel permite formatear los datos provenientes del body
      de la petición HTTP POST y convertirlos a una entidad legible por todo el framework para 
      poder asignar datos en su orden definido.""" 
```
🔍 Revisa el archivo `peticiones_http_simulador.py` para mas detalles.

---
## ♻️ Peticiones PUT: Actualización de datos

La petición PUT nos permite actualizar completamente un recurso existente.
En este caso, utilizaremos el ID del producto para identificar el elemento dentro de nuestra base de datos simulada (lista en Python).

El flujo sería:

1.  Recibir el ID como parámetro del endpoint.

2.  Verificar que el producto exista en la lista.

3.  Reemplazar los datos antiguos por los datos enviados en el body de la petición.

✅ Por buenas prácticas, siempre debemos validar la existencia del recurso antes de actualizarlo.

🔍 Ver completo en [peticiones_http_simulador.py](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/development/peticiones_http_simulador.py).


---
## 🗑️ Peticiones DELETE: Eliminación de datos

Por último, la petición DELETE se utiliza para eliminar un recurso específico.
Aquí también enviaremos el ID del producto a través del path del endpoint:
```python
## 💡 Ednpoint de petición DELETE
@app.delete("/producto/{id}") # ➡️ Utilizamos el envío de parámetros con PATH 
async def peticion_delete(id:int):
  ## Lógica
  #########
```
Este método removerá el elemento de nuestra lista que funcione como base de datos simulada.

🔍 Ver completo en [peticiones_http_simulador.py](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/development/peticiones_http_simulador.py).



---
### 📖 Siguiente paso → [07_http_status_code_endpoints.md](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/documentation/07_http_status_code_endpoints.md)  
#### En el siguiente archivo aprenderás sobre los `http status code` que permiten manejar correctamente la respuesta de cada endpoint.
---
# Sobre el autor  

Gracias por leer este primer capítulo 🔥.  

🔗 Conéctate conmigo en mis redes y sigue de cerca mi contenido:  
- [LinkedIn](https://www.linkedin.com/in/brayan-rafael-neciosup-bola%C3%B1os-407a59246/)  
- [GitHub](https://github.com/BrayanR03)  
- [Portafolio Web](https://bryanneciosup626.wixsite.com/brayandataanalitics)  


Nos vemos en el próximo archivo 👊🚀  