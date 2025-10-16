## 🧠 CAPÍTULO 11: AUTENTICACIÓN JWT (JSON WEB TOKEN)

En este capítulo veremos una **autenticación más segura**, basada en **JWT (JSON Web Token)**.  
A diferencia de la autenticación básica, JWT ofrece un **control más robusto y encriptado** del access token, garantizando una comunicación más confiable entre el cliente y el servidor.

---

### 🔐 Características principales de JWT

1. **Tiempo de duración (expiración)**  
   Define un período limitado durante el cual el usuario puede realizar las acciones permitidas.  
   Si el token expira, el usuario deberá **volver a autenticarse** para generar un nuevo access token.

2. **Estructura encriptada del access token (JWT)**  
   El token JWT está compuesto por **tres elementos principales**:
   - **Access Token:** Contiene la información cifrada que autentica al usuario.
   - **Secret Key:** Clave secreta utilizada por el backend para validar la autenticidad del token.
   - **Algoritmo:** Método criptográfico usado para firmar el token (el más común es **HS256**).

   Cada JWT está dividido en **tres secciones codificadas en Base64**:


---

### ⚙️ Instalación de librerías necesarias

Antes de comenzar con el código, instalemos las librerías necesarias:

```bash
pip install pyjwt              # ⬅️ Librería para manejar tokens JWT
pip install passlib[bcrypt]  # ⬅️ Librería para cifrar contraseñas mediante algoritmos seguros
```
---
### 🔎 Flujo de trabajo de la autenticación JWT (JSON Web Token)

La estructura del flujo JWT es similar a la autenticación básica, pero con pasos adicionales para encriptar, desencriptar y validar el token.
En el archivo `usuarios.py` dentro de 
[API_auth_jwt/](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/development/API_auth_jwt/routers/usuarios.py)
encontraremos más detalles del código. A continuación, se explican los pasos específicos del flujo JWT:

---

🧩 Paso 1. Importar las librerías necesarias
```python
import jwt  # ⬅️ Librería principal para manejo de JSON Web Tokens
from jwt.exceptions import InvalidTokenError  # ⬅️ Permite manejar errores de tokens inválidos
from passlib.context import CryptContext  # ⬅️ Permite utilizar un algoritmo de encriptación
```
---

🔑 Paso 2. Establecer en qué endpoint se generará el ACCESS TOKEN
(Paso similar al visto en la autenticación básica.)

---

⚙️ Paso 3. Definir variables constantes para los parámetros de JWT

Es buena práctica definir las variables de configuración como constantes globales.
```python
ALGORITHM = "HS256"              # Algoritmo de encriptación
ACCESS_TOKEN_DURATION = 1        # Duración del token en minutos
SECRET = "exampleSecret"         # Llave secreta del backend (⚠️ No subir al repositorio público)
```
* 💡 La SECRET KEY puede generarse de forma segura con el siguiente comando:
    ```bash
        openssl rand -hex 32
    ```
---

🧮 Paso 4. Definir el contexto de encriptación
```python
crypt = CryptContext(schemes=["bcrypt"])
```

---

🔐 Paso 5. Definir endpoint /login y lógica de acceso

Esta función permite generar y retornar el access token JWT, validando las credenciales del usuario y encriptando el token.

```python
@router_usuarios.post("/login", status_code=status.HTTP_200_OK)  # ⬅️ Establecemos el endpoint "/login"
async def login(form: OAuth2PasswordRequestForm = Depends()):     # ⬅️ Captura de credenciales con seguridad
    # 💡 Buscar usuario en base al username
    # Lógica ...

    # 💡 Validar existencia del usuario
    # Lógica ...

    # 💡 Validar contraseña mediante crypt.verify()
    # Lógica ...

    # --- ✅ Definir ACCESS TOKEN JWT ---

    # Paso A). Definir tiempo de expiración
    tiempo_expiracion_access_token = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_DURATION)
    # ➡️ datetime.now(): Retorna fecha y hora actual del servidor
    # ➡️ timezone.utc: Define zona horaria estándar
    # ➡️ timedelta: Define el tiempo de expiración del token

    # Paso B). Crear cuerpo del JWT
    access_token = {
        "sub": usuario.username,
        "exp": tiempo_expiracion_access_token
    }

    # Paso C). Encriptar JWT
    return {
        "access_token": jwt.encode(access_token, key=SECRET, algorithm=ALGORITHM),
        "token_type": "bearer"
    }
```
* ✅ Si todo fue correcto, se retornará un ACCESS TOKEN encriptado con la información del usuario.
---

🧠 Paso 6. Validar que el ACCESS TOKEN sea verídico

Esta función valida el token recibido, desencriptándolo y verificando su autenticidad y vigencia.
```python
async def auth_user_jwt(token: str = Depends(oauth2)):  # ⬅️ token generado en el paso 5
    # 💡 Excepción predeterminada para manejo de errores
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autenticación inválidas",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        # 💡 Desencriptar el token y obtener el usuario
        username = jwt.decode(token, key=SECRET, algorithms=[ALGORITHM]).get("sub")

        if username is None:
            raise exception

    except InvalidTokenError:
        raise exception

    # ---- Si todo fue validado correctamente, se retorna el usuario sin datos sensibles
    # Lógica ...
```
---

⚖️ Paso 7. Aplicar reglas de negocio al usuario autenticado
```python
async def current_user(usuario: Usuario = Depends(auth_user_jwt)):  # ⬅️ token validado como parámetro
    # 💡 Validaciones de negocio (roles, permisos, estado, etc.)
    # Lógica ...

    # ✅ Retornar datos del usuario (sin información sensible)
    return usuario

```
---
🔒 Paso 8. Acceso a los recursos protegidos de la API

(Paso similar al visto en la autenticación básica.)

---

✅ Y listo. Ahora cuentas con una autenticación segura mediante JWT, con cifrado, expiración y validación controlada.


Revisar imágenes de ejecución: 
* [Login_Generacion_Access_Token_JWT.png](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/assets/Login_Generacion_Access_Token_JWT.png)
* [Acceso_Recurso_Protegido_Access_Token_JWT.png](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/assets/Acceso_Recurso_Protegido_Access_Token_JWT.png)


---
### 📖 Siguiente paso → [12_conexion_mongodb.md](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/documentation/12_conexion_mongodb.md)  
#### En el siguiente archivo aprenderás a conectarte a una base de datos NoSQL (MongoDB).
---
# Sobre el autor  

Gracias por leer este onceavo capítulo 🔥. Se acerca el fin de esta serie ... 🔚  

🔗 Conéctate conmigo en mis redes y sigue de cerca mi contenido:  
- [LinkedIn](https://www.linkedin.com/in/brayan-rafael-neciosup-bola%C3%B1os-407a59246/)  
- [GitHub](https://github.com/BrayanR03)  
- [Portafolio Web](https://bryanneciosup626.wixsite.com/brayandataanalitics)  


Nos vemos en el próximo archivo 👊🚀  