from fastapi import status ## ⬅️ Importamos librería para el status 
from fastapi import HTTPException ## ⬅️ Importamos librería para el manejo correcto de errores en los endpoints
from pydantic import BaseModel ## ⬅️ Importamos librería para el formato adecuado de datos
from fastapi import APIRouter ## ⬅️ Importamos librería APIRouter para organizar y modularizar el código de una API.

## 💡 Librerías de Autenticación
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm
import jwt ## ⬅️ Librería de JWT (JSON WEB TOKEN)
from jwt.exceptions import InvalidTokenError ## ⬅️ Librería que permite manejar el error de un token inválido
from jwt.exceptions import ExpiredSignatureError ## ⬅️ Librería que permite manejar el error de un token expirado
from passlib.context import CryptContext ## ⬅️ Librería que permitirá utilizar el algoritmo de encriptación en un contexto

from fastapi import Depends ## ⬅️ Librería que permite establecer que una función depende
                            ##     de el resultado de otra función. 

from datetime import datetime  ## ⬅️ Librería que permite el manejo de fecha y hora
from datetime import timedelta ## ⬅️ Librería que permite realizar cálculos entre fechas
from datetime import timezone  ## ⬅️ Librería que permite traer la fecha y hora en base a una zona de localización

## ✅ Router generado para instanciar en main.py
router_usuarios = APIRouter(
    prefix="/usuarios",
    responses={404:{"message":"Ruta no encontrada"}}, 
    tags=["usuarios"] 
)

## 💡 Permite establecer que en el endpoint /login se generará y retornará un access_token.
oauth2 = OAuth2PasswordBearer(tokenUrl="login") ## ✅ Establece el contexto de autenticación y autorización en FastAPI.



## ----- Definiendo variables constantes que serán definidas para su uso constante (Buenas prácticas)

ALGORITHM = "HS256" ## ⬅️ Algoritmo establecido almacenado en una variable constante
ACCESS_TOKEN_DURATION = 1 ## ⬅️ Tiempo de duración del access token en minutos almacenado en una variable constante
SECRET = "12345" ## ⬅️ Llave secreta que solo el backend conoce y permite la encriptación / desencriptación segura (se generó con: openssl rand -hex 32)
## 💡 En este caso, yo he modificado la secret para evitar algún intento de hackeo.
## RECUERDA QUE SI TIENES UN PROYECTO EN GITHUB, NO DESPLIEGUES ESTA LLAVE SECRETA.


## ---- Definiendo contexto de encriptación mediante el algoritmo
crypt = CryptContext(schemes=["bcrypt"])


## ✅ Clase Usuario que hereda el formato de BaseModel
class Usuario(BaseModel):
    nombre : str
    apellido : str
    edad : int
    username : str
    disabled : bool

## ✅ Clase UsuarioBD que permite exponer solo lo necesario para la bd
class UsuarioBD(Usuario):
    password : str
  ## 💡 Creamos esta clase adicional que hereda de la anterior para poder exponer
  ##    los atributos necesarios al momento de la autenticación del usuario y no
  ##    exponer información sensible como el password en las respuestas de la API.


## ✅ Base de Datos simulada.

usuarios_bd = {
    "rcero3":{
        "nombre":"Brayan ",
        "apellido":"Neciosup",
        "edad":20,
        "username":"rcero3",
        "disabled": False,
        "password":"$2a$12$ddZlf1469ksLHloQ6z6r6.HjdG0AfV5hjYww95IsAyyGzUvg.ZSbi" ## En este caso la contraseña será encriptada (Desencriptada es: 12345)
    },
    "rcero2":{
        "nombre":"Brayan",
        "apellido":"Neciosup 2",
        "edad":25,
        "username":"rcero2",
        "disabled": True,
        "password":"$2a$12$Zhzz9fZLUoELtB8PGM4yrOKQdeFCGKgFgxdpVjPkOwuFMQAS3ivDC" ## En este caso la contraseña será encriptada (Desencriptada es: 54321)
    }
}

## ✅ Función que permite realizar la búsqueda de un usuario en base a su "username"
## 💡 Importante: En esta función retornamos valores escenciales para el escenario de BD,
##                es decir, retornamos el password en el objeto para su posterior validación.
def buscar_usuario_bd(username:str):
    return UsuarioBD(**usuarios_bd.get(username))

## ✅ Función que permite realizar la búsqueda de un usuario en base a su "username".
## 💡 Importante: En esta función retornamos valores escenciales para el escenario de datos del usuario,
##                es decir, retornamos los campos necesarios para su uso.
def buscar_usuario(username:str):
    return Usuario(**usuarios_bd.get(username))

##==== El uso de "**" permite el desempaquetamiento de los valores y su asignación a cada atributos de las clases

## ✅ Función que permite validar el ACCESS TOKEN mediante su desencriptación y
##    que recibe respuesta del token generado por la ruta (/login) que oauth2 había establecido.
async def auth_user_jwt(token : str = Depends(oauth2)):
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Credenciales de autenticación inválidas",
                            headers={"WWW-Authenticate":"Bearer"}) ## Al ser un error muy común, lo almacenamos en una variable para reutilizar código.
    
    ## 💡 Validamos que el token sea correcto
    try:
        
        username = jwt.decode(token,key=SECRET,algorithms=[ALGORITHM]).get("sub") ## 💡 Desencriptamos el ACCESS TOKEN y extraemos su cuerpo (username)
        if username is None: ## 💡 Validamos que el username no sea un vacío
            raise exception
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_408_REQUEST_TIMEOUT,detail="El token ha expirado",headers={"WWW-Authenticate":"Bearer"})
    
    except InvalidTokenError:
        raise exception

    return buscar_usuario(username) ## 💡 Si todo se validó correctamente, llamamos a la función buscar_usuario y
                                    ##    retornamos los datos completos de ese usuario.


## ✅ Función que recibe respuesta de los datos de usuario de la función auth_user_jwt().
async def current_user (usuario:Usuario = Depends(auth_user_jwt)): ## ⬅️ Depends() permite establecer que, el token generado
                                                             ##    servirá como parámetro en esta función.

    ## ----- Realizamos validaciones de reglas de negocio para los usuarios.
    if usuario.disabled: ## 💡 Permite verificar que el usuario no esté inactivo
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Usuario Inactivo")
    
    ## ---- Si todo fue validado correctamente, se retorna el usuario con sus datos no sensibles (Ejemp. Sin password).
    return usuario


## ✅ Función establecida por oauth2 para el retorno de un ACCESS TOKEN, además
##     permite el inicio de sesión de los usuarios de manera segura gracias a OAuth2PasswordRequestForm.
@router_usuarios.post("/login",status_code=status.HTTP_200_OK)
async def login(form:OAuth2PasswordRequestForm = Depends()): ## ⬅️ Depends() indica que esta función no dependerá del resultado
    usuario_bd = usuarios_bd.get(form.username)             ##     de otra función, pero, si será el que envie su respuesta a otra.
    ## 💡 Buscamos el usuario en base al username para validar su existencia.

    if not usuario_bd: ## 💡 Valida que el usuario exista
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="El usuario no es correcto")
    
    usuario = buscar_usuario_bd(form.username) ## 💡 Buscamos y almacenamos el usuario en base al username.
    if not crypt.verify(form.password,usuario.password) : ## 💡 Valida que la contraseña en texto plano sea igual a la
                                                          ##    contraseña encriptada en la BD simulada.
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="La contraseña es incorrecta")
    
    ## --- ✅ Definiendo ACCESS TOKEN JWT
    
    ##-- Paso A). Definir el tiempo de expiración
    tiempo_expiracion_access_token = datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_DURATION)
        ## ➡️ datetime.now(): Permite retornar la fecha y hora del servidor de internet (No es la misma de nuestra zona local).
        ## ➡️ timeszone.utc: Permite retornar la fecha y hora de nuestra zona local y redefinir el datetime.now().
        ## ➡️ timedelta(minute=ACCESS_TOKEN_DURATION): Permite agregar un minuto a la fecha y hora de nuestra zona local
    
    ##-- Paso B). Definir JWT
    access_token = {
        "sub": usuario.username,
        "exp": tiempo_expiracion_access_token
    }
    
    ##-- Paso C). Encriptar JWT
    return {"access_token":jwt.encode(access_token,key=SECRET,algorithm=ALGORITHM),"token_type":"bearer"}
        ## ➡️ jwt.encode(): Permite encriptar el access token, a través de una llave y algoritmo.
        ## ➡️ key: Es la llave que encriptará el access token.
        ## ➡️ algorithm: Es el algoritmo utilizado para encriptar el access token.


    ## ---- Si todo fue correcto, retornamos un ACCESS TOKEN. En este caso, es un ACCESS TOKEN sigue siendo el username, pero, encriptado.
    
    
## ✅ Función protegida por la autenticación mediante el ACCESS TOKEN,
##     es decir, si el ACCESS TOKEN no es correcto, no podemos acceder a los recursos
##     que brinde este endpoint.
@router_usuarios.get("/users/me")
async def user_me(usuario:Usuario = Depends(current_user)): ## ⬅️ Depends() indica que esta función dependerá de una respuesta
    return usuario                                          ##    de otra función, en este caso current_user.


## ✅ LEVANTAR ESTA API: En este caso, levantaremos las APIs desde el archivo principal (main).