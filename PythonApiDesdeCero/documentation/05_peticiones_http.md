# 📌 CAPÍTULO 05. PETICIONES HTTP EN LA API

Cuando hablamos de **operaciones realizadas a través de Internet**, como el ingreso a la página oficial de GitHub o el registro de un usuario en un formulario, todas ellas se manejan mediante **peticiones HTTP**.  

Estas peticiones dependen directamente del **objetivo de la operación** que se quiere realizar. En el contexto de las APIs, las más utilizadas son:

- **GET** → Obtener recursos.
- **POST** → Crear recursos.
- **PUT** → Actualizar recursos.
- **DELETE** → Eliminar recursos.

---

## 🌐 Endpoints y su importancia en una API

Para entender mejor cómo funcionan estas peticiones en **FastAPI**, debemos primero comprender el concepto de **endpoint**.

🔹 Un **endpoint** es una **ruta de acceso a los recursos de un sistema**. A través de este, los desarrolladores *front-end* (ya sea web o móvil) pueden conectarse al servidor para enviar o recibir información.  

En **FastAPI**, un endpoint se construye a partir de:
1. Una **función**.
2. Un **decorador** proporcionado por el framework.

> ⚡ **Dato importante**: un *decorador* en Python es una funcionalidad adicional que se aplica sobre una función. En FastAPI, los decoradores permiten asociar una ruta HTTP a la función que procesará la petición.

---

## 🛠️ Sintaxis de un Endpoint en FastAPI

La forma general de declarar un endpoint en FastAPI es:

```python
@nombre_contexto_fast_api.peticion_http("RutaRecursoServidor")
async def nombre_funcion_endpoint():
    return {"message": "Hola Mundo desde FastAPI!!!"}
```

#### 📌 Es un estándar que los endpoints devuelvan datos en formato JSON.  En Python, un JSON se representa como un diccionario {clave: valor}.

## 🛠️ Ejemplo de un Endpoint en FastAPI

```python
from fastapi import FastAPI  # Importamos la librería FastAPI

app = FastAPI()  # Creamos el contexto de FastAPI, la instancia usada por Uvicorn

@app.get("/")  
# Aquí usamos la petición GET con la ruta por defecto ("/").
# Esta ruta indica el acceso principal al servidor a través de la API.
async def main():
    return {"message": "Hola Mundo desde FastAPI!!!"}  
    # En este caso, el recurso que devolvemos es un JSON básico.
```

## 📌 Resumen

- Un endpoint conecta al frontend con los recursos del servidor mediante una API.

- Los decoradores de FastAPI asocian rutas y métodos HTTP a funciones específicas.

- Todo endpoint debe retornar datos en formato JSON.

- Las peticiones más comunes son: GET, POST, PUT y DELETE.

Ahora bien, una vez que ya conocimos todo lo referente a un `endpoint` podemos revisar el archivo [peticiones_http.py](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/development/peticiones_http.py) directamente para un mayor detalle de cada petición HTTP.

---
### 📖 Siguiente paso → [06_logica_peticiones_http.md](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/documentation/05_peticiones_http.md)  
#### En el siguiente archivo aprenderás a manejar lógica en cada petición http que utilizaremos en la API a desarrollar, mediante datos simulados.
---
# Sobre el autor  

Gracias por leer este primer capítulo 🔥.  

🔗 Conéctate conmigo en mis redes y sigue de cerca mi contenido:  
- [LinkedIn](https://www.linkedin.com/in/brayan-rafael-neciosup-bola%C3%B1os-407a59246/)  
- [GitHub](https://github.com/BrayanR03)  
- [Portafolio Web](https://bryanneciosup626.wixsite.com/brayandataanalitics)  


Nos vemos en el próximo archivo 👊🚀  

