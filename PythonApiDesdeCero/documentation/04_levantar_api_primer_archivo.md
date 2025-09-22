# 📌 CAPÍTULO 04. LEVANTAR API EN UN PRIMER ARCHIVO

Ahora sí, ¡vamos a escribir nuestro primer código! 🐍⚡  
En todo sistema (web, móvil, etc.) siempre existe un archivo principal, comúnmente llamado **main**, 
que se encarga de iniciar la aplicación y coordinar los demás módulos que forman parte del proyecto.  

En nuestro caso, **main.py** será el punto de entrada de la API. Aquí definiremos la instancia 
principal de **FastAPI** y levantaremos el servidor con **Uvicorn**.  

---

### 📌 Pasos para crear el archivo principal  

#### 1. Crear `main.py`  
Dentro de la carpeta de desarrollo (`development`), crea un archivo llamado **main.py**.  
con la extensión del lenguaje utilizado en este proyecto "python".

#### 2. Escribir el código inicial  
Dentro del archivo `main.py` debemos ir codificando ciertas lineas para que nuestra API tenga un funcionamiento
correcto (Puedes verificar el archivo [main.py](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/development/main.py) directamente para un mayor detalle).

```bash

from fastapi import FastAPI ## Librería FastAPI

app = FastAPI() ## Contexto de FastAPI y nombre de instancia utilizado en uvicorn

@app.get("/") ## Ruta por defecto 
async def main():
    return {"message":"Hola Mundo desde FastAPI!!!"}
```
#### 3. Levantar el servidor con Uvicorn
En la terminal, debemos aseguranos que apunte a la carpeta donde se encuentra nuestro archivo **main.py**
y escribimos el siguiente comando:

```bash
uvicorn main:app --reload
```
Como vemos, en el comando para levantar el servidor uvicorn colocamos el nombre del archivo `main`
seguido del contexto o instancia de la librería FastAPI `app`. Sin embargo, podemos utilizar
nombres diferentes, pero, por buenas prácticas dejamos que sea de esta manera.

Además, se utiliza el **--reload** permitiendo que el servidor se reinicie automáticamente cada 
vez que hagamos un cambio en el código, sin necesidad de reiniciarlo manualmente.

Si todo salió bien, en la terminal verás que el servidor se levantó correctamente. Y puedes 
acceder a la API desde tu navegador en:

```bash
http://127.0.0.1:8000

http://localhost:8000
```
Verificar imagenes [salida_terminal.png](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/assets/salida_terminal.png) y [navegador_respuesta.png](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/assets/navegador_respuesta.png)



#### 📖 Siguiente paso → [05_peticiones_http.md](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/documentation/05_peticiones_http.md)  
##### En el siguiente archivo aprenderás sobre las peticiones http que utilizaremos en la API a desarrollar.
---

# Sobre el autor  

Gracias por leer este cuarto capítulo 🔥.  

🔗 Conéctate conmigo en mis redes y sigue de cerca mi contenido:  
- [LinkedIn](https://www.linkedin.com/in/brayan-rafael-neciosup-bola%C3%B1os-407a59246/)  
- [GitHub](https://github.com/BrayanR03)  
- [Portafolio Web](https://bryanneciosup626.wixsite.com/brayandataanalitics)  


Nos vemos en el próximo archivo 👊🚀  