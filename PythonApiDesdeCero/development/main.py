
"""
    💡 Importante: Todas las librerías que instalemos mediante pip install ...
        siempre debemos de importarlas para poder utilizarlas. 
"""
from fastapi import FastAPI ## Librería FastAPI

"""
    💡 Importante: El contexto de FastAPI es la instancia que tenemos
       que realizar a la librería para poder utilizarla. Es como cuando
       instanciamos una Clase en cualquier otro lenguaje de programación
       (incluyendo este mismo). 
"""
app = FastAPI() ## Contexto de FastAPI

"""
    💡 Importante: Las rutas y métodos HTTP veremos en próximos capítulos, sin embargo,
        para poder verificar el funcionamiento correcto de nuestra API, utilizaremos
        la ruta por defecto "/", es decir, la ruta donde todo sistema web, backend, entre otros
        accede primeramente. Es como la puerta de una casa... sencilla analogía...

"""
@app.get("/") ## Ruta por defecto 
async def main():
    return {"message":"Hola Mundo desde FastAPI!!!"} ## El mensaje devuelto tiene el formato JSON(JavaScript Object Notation)
                                                     ## El cuál es un estándar utilizado en desarrollo web(backend-frontend)

"""
    ¿Porque las funciones estan presentes en las APIs en Python?:
    - Esto se debe a que las funciones permiten encapsular lógica que podemos
      utilizar cada vez que llamemos a la ruta o endpoint de la API.
    - Los endpoint son el punto de entrada a los recursos dentro de la API,
      ya sea imagenes, videos, datos, entre otros.
    - Además, deben ser asíncronas "async" para que el resto del sistema funciones
      sin ningún problema ante la demora de un endpoint.
"""