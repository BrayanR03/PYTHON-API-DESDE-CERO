# 📌 CAPÍTULO 02: VIRTUAL ENVIRONMENTS

En Python, cada proyecto puede requerir diferentes librerías y versiones.  
Un error común es instalar dependencias de forma global en el sistema, lo que puede provocar **conflictos** entre proyectos.

### ❌ El problema sin entornos virtuales
Imagina lo siguiente:  
- En un proyecto de **Data Analysis** usas `pandas 3.0`.  
- Meses después, inicias un proyecto de **Machine Learning** que requiere `pandas 4.0`.  

Si ambos proyectos comparten el mismo entorno global, instalar una versión sobrescribirá a la otra.  
Esto genera errores, funciones deprecadas y la necesidad de instalar/desinstalar paquetes constantemente, volviendo el trabajo insostenible.

### ✅ La solución: Virtual Environments
Un **virtual environment** (entorno virtual) es un espacio aislado que guarda todas las dependencias específicas de un proyecto.  
De esta forma:  
- Tu proyecto de **Data Analysis** mantiene `pandas 3.0`.  
- Tu proyecto de **Machine Learning** mantiene `pandas 4.0`.  

Cada uno dentro de su propia “caja”, sin interferir entre sí.  

---

## 🚀 Pasos para crear un Virtual Environment en tu proyecto

1. **Crea una carpeta para tu proyecto**  
   Ejemplo: `ApiDesdeCero`.

2. **Abre tu editor de código**  
   (Visual Studio Code u otro de tu preferencia).  

3. **Arrastra la carpeta del proyecto al editor**  
   y abre una **terminal** asegurándote de que la ruta apunte a tu carpeta recién creada.  

4. **Ejecuta el comando para crear el entorno virtual**  

   ```bash
   # Sintaxis
   python -m venv nombreVirtualEnv

   # Ejemplo (convención recomendada)
   python -m venv venv

5. **Activar el entorno virtual**
    Dependiendo del sistema operativo, la activación se realiza de la siguiente forma:

    - **Windows (CMD o PowerShell):**
    ```bash
    venv\Scripts\activate

    - **En macOS/Linux:**
    ```bash
    source venv/bin/activate

6. **Configurar el intérprete en tu editor**

    Si trabajas con Visual Studio Code, al activar el entorno, VSCode puede sugerirte usar el nuevo intérprete.
    En caso contrario, puedes seleccionarlo manualmente:

    Si usas Windows:
    
        PASO A). Abre el Command Palette (Ctrl + Shift + P).

        PASO B). Escribe Python: Select Interpreter.

        PASO C). Selecciona el intérprete asociado a tu venv (normalmente aparece como la primera opción).

        Con esto, tu proyecto queda completamente vinculado al entorno virtual.


📖 **Siguiente paso →** [03_instalacion_librerias.md](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/documentation/03_instalacion_librer%C3%ADas.md)  
En el siguiente archivo aprenderás a instalar las **librerías y dependencias** necesarias para el desarrollo del proyecto.

---

# Sobre el autor  

Gracias por leer este primer capítulo 🔥.  

🔗 Conéctate conmigo en mis redes y sigue de cerca mi contenido:  
- [LinkedIn](https://www.linkedin.com/in/brayan-rafael-neciosup-bola%C3%B1os-407a59246/)  
- [GitHub](https://github.com/BrayanR03)  
- [Portafolio Web](https://bryanneciosup626.wixsite.com/brayandataanalitics)  


Nos vemos en el próximo archivo 👊🚀  