"""Definir dos conjuntos que almacenen cada uno una serie de lenguajes de programación. Efectuar las cuatro operaciones básicas con dichos conjuntos."""

#Creamos los dos conjuntos
lenguajes1={"C", "Pascal", "PHP", "Python"}
lenguajes2={"C++", "Java", "Python"}
#Union de ambos (OJO: tener en cuenta que no se agregan valores repetidos en las estructuras tipo conjunto)
union=lenguajes1 | lenguajes2
#Compara las similitudes entre ambos conjuntos
interseccion=lenguajes1 & lenguajes2
#Compara diferencia del primer conjunto respecto al segundo
diferencia=lenguajes1 - lenguajes2
#Analiza las diferencias entre ambos cojuntos
diferencia_simetrica=lenguajes1 ^ lenguajes2

#Mostramos resultados
print(f"Union: {union}")
print(f"Interseccion: {interseccion}")
print(f"Diferencia: {diferencia}")
print(f"Diferencia simetrica: {diferencia_simetrica}")
