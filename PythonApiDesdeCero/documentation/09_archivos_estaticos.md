# 📌 CAPÍTULO 09: ARCHIVOS ESTÁTICOS EN FASTAPI 🔙🔚🗃️

En este capítulo abordaremos el manejo de **archivos estáticos** en FastAPI.  
Estos archivos pueden ser imágenes, documentos, hojas de estilo, scripts, entre otros.

## ❌ El problema
FastAPI, por defecto, **no permite acceder directamente a las carpetas del backend** para consultar archivos estáticos.  
Por ejemplo, si tenemos una carpeta llamada `static` con subcarpetas `images` y `docs`, al intentar acceder a:
``` cmd
http://localhost:8000/static/images/UnionDatasetsColumnar.jpg
```

Obtendremos la respuesta:

```json
{"detail": "Not Found"}
```
📷 Revisar imagen: 
[RESULTADO_ARCHIVOS_ESTATICOS_SIN_EXPONER.png](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/assets/RESULTADO_ARCHIVOS_ESTATICOS_SIN_EXPONER.png)

Esto ocurre porque FastAPI protege el acceso directo a los directorios del servidor para evitar exponer información sensible.

## ✅ La solución: StaticFiles

FastAPI incluye el módulo `StaticFiles`, el cual nos permite exponer de manera controlada recursos estáticos a Internet.
De esta manera, podemos definir qué carpetas serán accesibles y bajo qué ruta.

* ⚠️ Importante: Aunque los recursos estáticos son públicos, debemos tener cuidado de no exponer archivos sensibles.

🔹 Importación

En `main.py` debemos importar:
```python
from fastapi.staticfiles import StaticFiles
```

🔹 Sintaxis General

```python
app.mount(
    path="/RutaEnInternet",
    app=StaticFiles(directory="CarpetaLocalEnBackend"),
    name="NombreInterno"
)
```
🔹 Ejemplo

Si tenemos una carpeta llamada `static` dentro de nuestro proyecto:

```python
app.mount(
    path="/static",
    app=StaticFiles(directory="static"),
    name="static"
)
```
Con esta configuración, todos los recursos dentro de la carpeta `static` estarán disponibles públicamente desde el servidor.

## 🌐 Probando el acceso

Ahora, al acceder nuevamente a la ruta:

```cmd
http://localhost:8000/static/images/UnionDatasetsColumnar.jpg
```
El archivo será servido correctamente.

📷 Revisar imagen: 
[RESULTADO_ARCHIVOS_ESTATICOS_EXPUESTO.png](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/assets/RESULTADO_ARCHIVOS_ESTATICOS_EXPUESTO.png)

## 📂 Organización recomendada

Una buena práctica es mantener una carpeta static/ con subcarpetas específicas:

```css
static/
 ├── images/
 ├── docs/
 └── css/
```
De esta manera, logramos una estructura clara y mantenible para nuestros recursos estáticos.

📌 Ver carpeta de ejemplo: 
[API_archivos_estaticos_expuestos/](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/development/API_archivos_estaticos_expuestos/)


---
### 📖 Siguiente paso → [10_autenticacion_basica.md](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/documentation/10_autenticacion_basica.md)  
#### En el siguiente archivo aprenderás sobre las autenticaciones en el lado del Backend y una explicación de una atenticación básica antes de entrar a JWT.
---
# Sobre el autor  

Gracias por leer este noveno capítulo 🔥.  

🔗 Conéctate conmigo en mis redes y sigue de cerca mi contenido:  
- [LinkedIn](https://www.linkedin.com/in/brayan-rafael-neciosup-bola%C3%B1os-407a59246/)  
- [GitHub](https://github.com/BrayanR03)  
- [Portafolio Web](https://bryanneciosup626.wixsite.com/brayandataanalitics)  


Nos vemos en el próximo archivo 👊🚀  