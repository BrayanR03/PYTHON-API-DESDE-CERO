# 📌 CAPÍTULO 03. INSTALACIÓN DE LIBRERIAS

En este capítulo nos enfocaremos en instalar las **primeras librerías necesarias** para nuestro proyecto.  
La idea es comenzar con lo esencial, evitando instalar todo desde el inicio. Conforme avancemos en los 
próximos capítulos, iremos añadiendo nuevas dependencias que nos permitan escalar y mejorar la API de forma ordenada.  
---
### 📌 Pasos para instalar librerías

#### 1. Abrir la terminal  
Abre una terminal desde **Visual Studio Code** o tu editor de preferencia, y asegúrate de apuntar a la carpeta raíz de tu proyecto.  

---

#### 2. Activar el entorno virtual  
Verifica que te encuentras dentro del entorno virtual que creamos previamente (`venv`).  
Esto es importante para que las librerías se instalen únicamente en este entorno y no en el intérprete global de Python de tu sistema.  

Ejemplo de activación en Windows:
```bash
venv\Scripts\activate

```

Ejemplo de activación en Linux/Mac:
```bash
source venv/bin/activate

```

#### 3. Instalar FastAPI y Uvicorn
Para iniciar, instalaremos FastAPI junto con Uvicorn, el servidor local que nos permitirá ejecutar la API.

Ejecuta el siguiente comando en la terminal:
```bash
pip install fastapi[all]

```
Con este comando se instala:

    * FastAPI → framework principal para crear nuestra API.

    * Uvicorn → servidor ASGI que nos permitirá ejecutar la API en localhost.

Y tranquilo, todas las letras, números que veas scrollear en tu terminal son todos los paquetes internos de FastAPI.
No te estan hackeando!!.

🔍 ¿Por qué usar Uvicorn?

Toda aplicación (API, base de datos o sistema web/móvil) necesita ejecutarse en un servidor.
En este caso, Uvicorn nos brinda un servidor ligero y optimizado para FastAPI, permitiéndonos 
levantar el proyecto en modo local y validar su funcionamiento conforme avancemos en la 
construcción de nuestra API.


📖 **Siguiente paso →** [04_levantar_api_primer_archivo.md](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/documentation/04_levantar_api_primer_archivo.md)  
En el siguiente archivo aprenderás a levantar la API mediante la creación del archivo principal **main**.
---

# Sobre el autor  

Gracias por leer este primer capítulo 🔥.  

🔗 Conéctate conmigo en mis redes y sigue de cerca mi contenido:  
- [LinkedIn](https://www.linkedin.com/in/brayan-rafael-neciosup-bola%C3%B1os-407a59246/)  
- [GitHub](https://github.com/BrayanR03)  
- [Portafolio Web](https://bryanneciosup626.wixsite.com/brayandataanalitics)  


Nos vemos en el próximo archivo 👊🚀  