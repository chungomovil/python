"""Se tiene una lista de nombres de personas. Generar otra lista cuyos elementos sean a su vez listas con dos nombres cada uno.

Tener en cuenta que nunca se debe combinar el mismo nombre dos veces."""

#Creamos la lista iniciar de nombres
nombres=["felipe", "paco", "juan", "eustaquio", "teodoro"]

#Creamos dos bucles en la comprension de la lista, la tupla almacenara el valor retornado en cada uno de los bucles
pareja=[(nombre1, nombre2) for nombre1 in nombres for nombre2 in nombres if nombre1!=nombre2]

#mostramos resultado
print(pareja)


