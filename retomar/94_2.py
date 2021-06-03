"""Se tiene una lista con un conjunto de tuplas con los nombres y edades de personas:

personas=[('pedro',33),('ana',3),('juan',13),('carla',45)]

Generar una lista con las personas mayores de edad."""

#Creamos la lista principal
personas=[('pedro',33),('ana',3),('juan',13),('carla',45)]
#Realizamos el algoritmo con compresion de listas
mayoredad=[(nombre, edad) for nombre,edad in personas if edad>=18]
#mayoredad=[persona for persona in personas if persona[1]>=18] // OTRA FORMA DE HACERLO

#Informamos del resultado
print(f"Lista principal: {personas}\nLista mayores edad: {mayoredad}")

