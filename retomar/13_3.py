"""Solicitar el ingreso de una clave por teclado y almacenarla en una cadena de caracteres. 
Controlar que el string ingresado tenga entre 10 y 20 caracteres para que sea válido, 
en caso contrario mostrar un mensaje de error."""

error=True

while error==True:
    contador=0
    clave=input("introducir una clave (sin espacios): ")
    for y in range(len(clave)):
        if clave[y]==" ":
            contador+=1
    if contador==0:
        error=False

if len(clave)>=10 and len(clave)<=20:
    print("*****clave almacenada correctamente*****")
else:
    print("*ERROR*. Introducir clave de longitud de 10 a 20 caracteres.")