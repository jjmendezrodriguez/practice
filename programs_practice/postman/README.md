# Postman

Vamos aprender postman como funciona y como usarlo.

Nuesta referencia fue __frikyland.com__

## Formato JSON

Formato indepoendiente de texto del lenguaje, ideal para el intercambio de datos y es universal para todos los lenguajes de programacion. (todos los lenguajes entienden el formato)

__Ejemplo:__

    variable = {
        "key": 23, "key": "valor", "key":["valores", "valores2"]
        }

Puede ser tan complejo como lo desees esto es solo un ejemplo. Tambien puedes tener listas dentro de json. Es el lenguaje utilisado para que diferentes lenguajes de comuniquen.

Una coleccion de pares de nombre/valor. En varios lenguajes esto conocido como un objeto, registro, estructura, diccionario, tabla hash, lista de claves o un arreglo asociativo.

Una lista ordenada de valores. En la mayoria de los lenguajes, esto se implementa como arreglos, vectores, listas o secuencias.

## Formato HTTP

- __Cliente sevidor:__ Hacemos peticiones al servidor, computador al servidor, protocolo HTTP.

Para intercomabiar informacion entre cliente y servidor siguendo las normas, esta definido por cabeceras.

__codigos de respuesta:__

Rango de 100: Respuesta Informativa
Rango de 200: Respuesta Correcta
Rango de 300: Redireccion
Rango de 400: Error del Cliente (404 no exixte error comun)
Rango de 500: Error de Servidor

__Verbos:__

GET: Obtener informacion del servidor
POST: Envia informacion al servidor
PUT: Actualizar informacion del servidor
DELETE: Eliminar informacion del servidor

## Que es postman

Descargala en `postman.com`

Construir y utilizar APIs simplifica el ciclo de vida para crearla mejores y mas rapidas. Ayuda a visualisarlo mejor.

__Para hacer pruebas con postman puedes usar:__

    https://postman-echo.com

__Headers:__

Alguna informacion se envia desde el header como los tokens para mayor seguridad y no pueda ser visible.

Port 443 es informacion encriptada.

__Collections:__

Herramienta para un conjunto de peticiones para poder guardarla a nuestro antojo.

__Fork:__

Para clonar

__Tokens:__

una llave de texto para que no pueda ser copiado y te da permisos, depende la configuracion son los permisos que tiene. Un formato para esto es Json Web Token (JWT).

