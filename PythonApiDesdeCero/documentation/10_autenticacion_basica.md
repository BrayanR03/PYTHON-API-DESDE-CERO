## 📌 CAPÍTULO 10. AUTENTICACIÓN BÁSICA EN FASTAPI 🔒

En este capítulo veremos una **autenticación básica** al momento de realizar un *login* en una ruta específica de nuestra API.  
Sin embargo, muchas veces como desarrolladores solemos confundir los términos **autenticar** y **autorizar**, pero no son lo mismo.  
Veamos la diferencia:

- **Autenticar:** permite al usuario acceder a una plataforma, sistema o aplicación a través de su usuario y contraseña.  
  Por ejemplo, cuando ingresamos a una plataforma de *streaming* o sistema interno, nos **autenticamos** cada cierto tiempo para validar nuestra identidad.

- **Autorizar:** define qué puede o no puede hacer un usuario dentro del sistema una vez autenticado.  
  Por ejemplo, un usuario puede tener permiso solo para visualizar información, pero no para subir, descargar o modificar archivos.  
  
En otras palabras, **autenticarse** valida la identidad del usuario, mientras que **autorizarse** define los permisos que tiene dentro de la aplicación. De esta manera, queda clara la diferencia entre ambos conceptos antes de continuar.

---

Por otro lado, debemos entender cómo se maneja la **autenticación en una API**, seguramente has escuchado conceptos como *access token*, *API keys*, entre otros. Estos temas los abordaremos más adelante con mayor detalle, 
en este capítulo nos enfocaremos en una **autenticación básica**, usando un *access token* simple.

---

### 🔐 Módulos de seguridad en FastAPI

Para ello utilizaremos los módulos internos de **seguridad y autenticación** que ofrece FastAPI:

```python
from fastapi.security import OAuth2PasswordBearer 
from fastapi.security import OAuth2PasswordRequestForm  
```

**OAuth2PasswordBearer**: permite establecer un contexto de autenticación y autorización en FastAPI, gestionando la ruta donde se generará y retornará un access token, por ejemplo, en el endpoint de login.

**OAuth2PasswordRequestForm**: actúa como un intermediario abstracto que captura las credenciales enviadas en el body de la petición (normalmente mediante un método POST), asegurando la recepción de los datos de usuario y contraseña de manera segura para su posterior verificación en la base de datos de la API.

---
### 🔎 Flujo de trabajo de la autenticación
Para comprender de forma completa cómo funciona una autenticación y cómo se gestiona el acceso a recursos protegidos, analizaremos el archivo `usuarios.py`, ubicado en la carpeta [API_auth_basica/](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/development/API_auth_basica/routers/). En este archivo se desarrolla todo el proceso correspondiente a una **autenticación básica** dentro de nuestra API.

Sin embargo, en este capítulo no solo veremos el código, sino que entenderemos **el orden de ejecución y la lógica interna** detrás de cada parte del archivo `usuarios.py`. Y puede surgir la pregunta: **¿por qué analizarlo paso a paso?**

Porque si realmente queremos entender cómo funciona la autenticación, debemos seguir el **flujo completo** que recorre la información: 
* Desde el momento en que el usuario envía sus credenciales (usuario y contraseña) en el login.
* Hasta cómo esas credenciales son verificadas y finalmente permiten o deniegan el acceso a recursos protegidos.

El archivo ya cuenta con una estructura limpia y bien organizada, pero aquí lo abordaremos **desde una perspectiva didáctica**, explicando en qué orden ocurre cada parte del proceso para que el funcionamiento sea completamente claro antes de centrarnos en el código.

Veamos el flujo paso a paso:

---

### 🧩 **Paso 1. Establecer en qué endpoint se generará el ACCESS TOKEN**

💡 Gracias a `OAuth2PasswordBearer`, se puede establecer que en el endpoint `/login` se generará y retornará un **access_token**.

```python
oauth2 = OAuth2PasswordBearer(tokenUrl="login")
```

### ⚙️ Paso 2. Definir endpoint /login y lógica de acceso
✅ Esta función, establecida por oauth2, permite el retorno de un ACCESS TOKEN y el inicio de sesión de los usuarios de manera segura, gracias a OAuth2PasswordRequestForm, que actúa como intermediario para recibir las credenciales.
```python
@router_usuarios.post("/login",status_code=status.HTTP_200_OK) # ⬅️ Establecemos el endpoint "/login".

async def login(form:OAuth2PasswordRequestForm = Depends()): ## ⬅️ Depends() indica que esta función no dependerá del resultado de otra función.
    ## 💡 Buscamos el usuario en base al username para validar su existencia.
          Lógica .....

    ## 💡 Valida que el usuario exista
          Lógica .....
    
    ## 💡 Valida que la contraseña sea correcta
          Lógica ....
        
    ##  ✅ Si todo fue correcto, retornamos un ACCESS TOKEN. En este caso, es un ACCESS TOKEN básico que es el username.
    return {"access_token":usuario.username,"token_type":"bearer"}
```

### 🧠 Paso 3. Validar que el ACCESS TOKEN sea verídico

✅ Esta función recibe el token generado por la ruta /login, establecida previamente en el contexto de oauth2 (Paso 1).
```python
async def current_user (token:str = Depends(oauth2)): ## ⬅️ Depends() permite establecer que, el token generado (Paso 2) servirá como parámetro en esta función.
    
    ## Buscamos el usuario gracias al username que se retorna en el token.
      Lógica ....
    ## ----- Realizamos validaciones del token

      if not user: ## 💡 Validamos que el token sea correcto.
          raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Crredenciales de autenticación inválidas",
                              headers={"WWW-Authenticate":"Bearer"})
    
    ## ----- Realizamos validaciones de reglas de negocio para los usuarios.
       Lógica ....
    
    ## ---- Si todo fue validado correctamente, se retorna el usuario con sus datos no sensibles (Sin password).
       Lógica .... 

```
🔒 Paso 4. Llamar a los recursos protegidos de la API

✅ Esta función está protegida por autenticación mediante el ACCESS TOKEN.
Es decir, si el token no es correcto, no se podrá acceder a los recursos que brinde este endpoint.
```python
@router_usuarios.get("/users/me")
                                                               # ⬇️ Depends() indica que esta función depende del resultado de current_user (Paso 3).
async def user_me(usuario:Usuario = Depends(current_user)): 
    return usuario                                          
```
✅ Y listo, ya entendimos correctamente una autenticación básica.

Revisar imágenes de ejecución: 
* [Login_Generacion_Access_Token.png](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/assets/Login_Generacion_Access_Token.png)
* [Acceso_Recurso_Protegido_Access_Token.png](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/assets/Acceso_Recurso_Protegido_Access_Token.png)


---
### 📖 Siguiente paso → [11_autenticacion_jwt.md](https://github.com/BrayanR03/PYTHON-API-DESDE-CERO/blob/main/PythonApiDesdeCero/documentation/11_autenticacion_jwt.md)  
#### En el siguiente archivo aprenderás sobre una auntenticación con encriptación: JWT (Json Web Token).
---
# Sobre el autor  

Gracias por leer este décimo capítulo 🔥.  

🔗 Conéctate conmigo en mis redes y sigue de cerca mi contenido:  
- [LinkedIn](https://www.linkedin.com/in/brayan-rafael-neciosup-bola%C3%B1os-407a59246/)  
- [GitHub](https://github.com/BrayanR03)  
- [Portafolio Web](https://bryanneciosup626.wixsite.com/brayandataanalitics)  


Nos vemos en el próximo archivo 👊🚀  


