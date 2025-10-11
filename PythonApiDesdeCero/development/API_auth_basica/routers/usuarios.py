from fastapi import status ## ⬅️ Importamos librería para el status 
from fastapi import HTTPException ## ⬅️ Importamos librería para el manejo correcto de errores en los endpoints
from pydantic import BaseModel ## ⬅️ Importamos librería para el formato adecuado de datos
from fastapi import APIRouter ## ⬅️ Importamos librería APIRouter para organizar y modularizar el código de una API.

## 💡 Librerías de Autenticación
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm

from fastapi import Depends ## ⬅️ Librería que permite establecer que una función depende
                            ##     de el resultado de otra función. 


## ✅ Router generado para instanciar en main.py
router_usuarios = APIRouter(
    prefix="/usuarios",
    responses={404:{"message":"Ruta no encontrada"}}, 
    tags=["usuarios"] 
)

## 💡 Permite establecer que en el endpoint /login se generará y retornará un access_token.
oauth2 = OAuth2PasswordBearer(tokenUrl="login") ## ✅ Establece el contexto de autenticación y autorización en FastAPI.

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
        "password":"12345"
    },
    "rcero2":{
        "nombre":"Brayan",
        "apellido":"Neciosup 2",
        "edad":25,
        "username":"rcero2",
        "disabled": True,
        "password":"54321"
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


## ✅ Función que recibe respuesta del token generado por la ruta (/login) que 
##     oauth2 había establecido.
async def current_user (token:str = Depends(oauth2)): ## ⬅️ Depends() permite establecer que, el token generado
    user = buscar_usuario(token)                      ##    servirá como parámetro en esta función.
    ## Buscamos el usuario gracias al username que
    ## se retorna en el token.
    
    ## ----- Realizamos validaciones del token
    if not user: ## 💡 Validamos que el token sea correcto.
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Crredenciales de autenticación inválidas",
                            headers={"WWW-Authenticate":"Bearer"})
    
    ## ----- Realizamos validaciones de reglas de negocio para los usuarios.
    if user.disabled: ## 💡 Permite verificar que el usuario no esté inactivo
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Usuario Inactivo")
    
    ## ---- Si todo fue validado correctamente, se retorna el usuario con sus datos no sensibles (Ejemp. Sin password).
    return user


## ✅ Función establecida por oauth2 para el retorno de un ACCESS TOKEN, además
##     permite el inicio de sesión de los usuarios de manera segura gracias a OAuth2PasswordRequestForm.
@router_usuarios.post("/login",status_code=status.HTTP_200_OK)
async def login(form:OAuth2PasswordRequestForm = Depends()): ## ⬅️ Depends() indica que esta función no dependerá del resultado
    usuario_bd = usuarios_bd.get(form.username)             ##     de otra función, pero, si será el que envie su respuesta a otra.
    ## 💡 Buscamos el usuario en base al username para validar su existencia.
        
    if not usuario_bd: ## 💡 Valida que el usuario exista
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="El usuario no es correcto")
    
    usuario = buscar_usuario_bd(form.username) ## 💡 Buscamos y almacenamos el usuario en base al username.
    
    if not form.password == usuario.password : ## 💡 Valida que la contraseña sea correcta
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="La contraseña es incorrecta")
    
    ## ---- Si todo fue correcto, retornamos un ACCESS TOKEN. En este caso, es un ACCESS TOKEN básico que es el username.
    return {"access_token":usuario.username,"token_type":"bearer"}


## ✅ Función protegida por la autenticación mediante el ACCESS TOKEN,
##     es decir, si el ACCESS TOKEN no es correcto, no podemos acceder a los recursos
##     que brinde este endpoint.
@router_usuarios.get("/users/me")
async def user_me(usuario:Usuario = Depends(current_user)): ## ⬅️ Depends() indica que esta función dependerá de una respuesta
    return usuario                                          ##    de otra función, en este caso current_user.


## ✅ LEVANTAR ESTA API: En este caso, levantaremos las APIs desde el archivo principal (main).