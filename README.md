# Before execute project
1. install requirements.txt
2. Execute pw_table.py for creating the database tables

# Creación de un API REST
La prueba consistirá en crear un simple API REST para un único recurso, la prueba se dividirá en una funcionalidad básica y en funcionalidades adicionales que sumarán puntos a la evaluación.

Este repositorio contiene los archivos base, los cambios realizados deben subirse en un repositorio propio, el link de ese repositorio debe enviarse por email.

## 1. Funcionalidad básica
Se desea un endpoint para poder administrar notas (crear y listar), los datos se guardará en una base de datos sqlite. Para ello se utilizarán los siguientes paquetes de Python.

peewee (ORM)
bottle (miniframework web)
Los campos que tendrá el modelo no son relevantes.

## 2. Funcionalidades adicionales
Las siguientes funcionalidades se construirán sobre la funcionalidad base.

### Serialización y validación

Se desea validar los datos que se reciben via POST y mostrar los errores al usuario que usa el API, serializar la lista de objetos para enviarlas como json. Para ello se utilizará la librería marshmallow.

### Usuario y Autentificación

Se desea que el API sea restringido mediante algún método de autenficación.

### JWT

Se desea que el usuario se autentifique mediante json web tokens, para ello se utializará la librería pyjwt

### Autorización

Se desea asociar una nota con un usuario, de tal manera que cada usuario solo pueda ver sus propias notas.

### Cliente del API

Se desea tener un cliente web que haga uso del API desde frontend (html y javascript).
