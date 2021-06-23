"""Confeccionaremos un script que intente recuperar una página HTML que no se encuentre en el servidor:

http://www.scratchya.com.ar/pythonya/ejercicio336/paginax.html
luego capturaremos la excepción 'HTTPError'"""

#Importamos los modulos de peticion y error de la libreria encargada de conectar a la web
from urllib import request
from urllib import error

#Filtramos el algoritmo que deseamos probar
try:
    #Realizamos la peticion al servidor web
    web=request.urlopen("http://www.scratchya.com.ar/pythonya/ejercicio336/paginax.html")
    
    #Leemos datos de la url
    datos=web.read()

    #Mostramos resultado
    print(datos)

#Procesamos excepcion
except error.HTTPError as err:
    #Mostramos el codigo de error devuelto
    print(f"ERROR -> Codigo de respuesta del servidor: {err.code}")
    
    #Mostramos la ruta que ha causado el error
    print(f"Direccion no encontrada: {err.filename}")


