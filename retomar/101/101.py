"""Definir un string en Python con la estructura interna de un archivo JSON.
Deserializar el string y convertirlo a una lista de Python. Luego volver a serializar la lista a un string."""

#Importamos el modulo de json
import json

#Creamos la cadena (con estructura de lista y dentro de ella varios diccionarios)
cadena="""[
    {"codigo":"1","descripcion":"tomate","precio":"2.90"},
    {"codigo":"2","descripcion":"judias","precio":"1.22"},
    {"codigo":"3","descripcion":"pepino","precio":"0.9"}
    ]"""

#Mostramos el tipo de dato de la cadena inicialmente
print("Formato inicial de la cadena:", type(cadena))
print(cadena)
#La deserializamos
cadena=json.loads(cadena)
#Mostramos el tipo de dato de la cadena deserializada
print("Formato deserializado de la cadena", type(cadena))
print(cadena)
#La serializamos
cadena=json.dumps(cadena)
#Mostramos el tipo de dato de la cadena serializada
print("Formato serializado de la cadena", type(cadena))
print(cadena)


