# Arquitectura simple de ingesta de datos iot
Este proyecto, es una arquitectua basica para recepciòn e ingesta de datos de sensores remotos, utilizando tecnologias como, MongoDB, Apache Kafka y FastAPI

![arquitectura_iot](https://user-images.githubusercontent.com/33732034/180153703-02c775fd-3906-42de-b301-9e2e37683b46.png)


Figura: 1.1: Arquitectura IoT, ingesta de datos

# Requerimientos indispensables
Docker, Python3.7+

# Pasos para ejecutar el proyecto
* El servidor de MongoDB y Apache Kafka, estan configurados en el archivo **docker-compose.yml** 
* La aplicacion con FastAPI se encuentra en el fichero src
* El simulador de sensor de temperatura, es el archivo  **cliente.py**



## Paso 1
Para encender  los servicios de MongoDB y Apache Fakfa

`$ docker-compose up`

## Paso 2
* Instalar dependecias y librerias necesarias para la app con FastAPI

`$ pip install -r requirements.txt`

* Comenzar la ejecucion de la app, por defecto el puerto es 8000

`$ cd src`

`$ uvicorn main:app` 


## Paso 3
Ejecutar el cliente una terminal nueva, por defecto el cliente tiene habilitado el envio de datos a la app server por el puerto 8000

`$ python3 cliente.py`

## Paso 4
* Despues de ejecutar los pasos anteriores, el  sensor simulado esta enviando datos correctamnete.
* Ingresar a la siguinete url en su navegador **localhost:8000/docs**
* Es la ruta de FastAPI para acceder a Swagger, en dicha ruta se encuentra el CRUD





