# 🚦 CAPÍTULO 8: ROUTERS EN FASTAPI

En este capítulo exploraremos **Routers** en una API con **FastAPI**.  
Hasta ahora hemos venido trabajando con **múltiples archivos de API**, donde en cada uno levantamos un servidor individual.  
Aunque funcional, **esta práctica no es recomendable**, pues rompe la organización y dificulta el mantenimiento a medida que el proyecto crece.

---

## 🧩 ¿Por qué usar Routers?

Cuando cada archivo (por ejemplo: `main.py`, `clientes.py`, `productos.py`) define su propio `FastAPI()` y levanta un servidor independiente:

- **Cada archivo funciona como una API aislada.**  
- Debes **levantar cada uno por separado** para que opere.  
- Existe el riesgo de **colisiones de puerto y rutas** si todos intentan ejecutarse al mismo tiempo.

> 💡 Imagina que para iniciar tu sistema completo debas levantar tres servidores distintos: uno para clientes, otro para productos y otro para ventas.  
> Esto **no escala** y complica el despliegue.

---

## 🏗️ La solución: Routers

Los **Routers** permiten:

1. **Centralizar la ejecución** en un solo archivo principal (`main.py`).
2. **Modularizar** la lógica en varios archivos (por ejemplo, `productos.py`, `usuarios.py`, `ventas.py`).
3. Mantener una **arquitectura limpia y escalable**.

Con Routers, el archivo `main.py` **lidera el proyecto**: levanta un solo servidor y **conecta** las rutas definidas en los demás módulos.

---

## 🗂️ Estructura sin Routers

En la carpeta [`API_sin_routers/`](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/development/API_sin_routers/) (dentro de `development`) podrías encontrar algo como:
``` css
development/
├─ API_sin_routers/
│ ├─ main.py
│ ├─ clientes.py
│ └─ productos.py
```

- Cada archivo (`main`, `clientes`, `productos`) contiene su **propia instancia** de `FastAPI()`:
```python
  from fastapi import FastAPI
  app = FastAPI()
```
* Esto significa que no existe relación entre ellos y, por tanto, cada uno debe levantarse de forma independiente.

## 🗂️ Estructura con Routers
En la carpeta [`API_con_routers/`](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/development/API_con_routers/):
``` css
development/
├─ API_con_routers/
│  ├─ main.py
│  ├─ routers/
│  │   ├─ clientes.py
│  │   └─ productos.py
```
Aquí, solo main.py levanta el servidor, mientras que los demás archivos son routers que se “enganchan” al main.

## 🚀 Beneficios de usar Routers

* Modularidad: Cada funcionalidad vive en su propio archivo.

* Escalabilidad: Agregar nuevas rutas es tan simple como crear un archivo y registrarlo en main.py.

* Mantenimiento sencillo: El código está ordenado y separado por contexto.

* Evita conflictos de puerto y rutas: Solo existe un servidor principal.

## 💡 Conclusión

 El uso de Routers en FastAPI permite:

* Centralizar el levantamiento del servidor.

* Organizar y escalar proyectos de forma profesional.

* Mantener una arquitectura limpia, ideal para entornos de producción.

* En resumen, APIRouter es la clave para convertir una API pequeña en una aplicación mantenible y lista para crecer.

---
### 📖 Siguiente paso → [09_archivos_estaticos.md](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/documentation/09_archivos_estaticos.md)  
#### En el siguiente archivo aprenderás sobre los `archivos estaticos` y como exponerlos en los endpoints.
---
# Sobre el autor  

Gracias por leer este octavo capítulo 🔥.  

🔗 Conéctate conmigo en mis redes y sigue de cerca mi contenido:  
- [LinkedIn](https://www.linkedin.com/in/brayan-rafael-neciosup-bola%C3%B1os-407a59246/)  
- [GitHub](https://github.com/BrayanR03)  
- [Portafolio Web](https://bryanneciosup626.wixsite.com/brayandataanalitics)  


Nos vemos en el próximo archivo 👊🚀  