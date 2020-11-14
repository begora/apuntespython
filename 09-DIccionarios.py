# asociacion clave:valor a cada valor que almacenamos se le asigna una clave unica,
# tipo de valor: cualquiera, incluso listas tuplas y otro diccionario
# orden es indiferente porque tienen una clave única
mydictionary={"Alemania":"Berlín", "Francia":"París", "España":"Madrid"}

#agregar elementos

mydictionary["Italia"]="Lisboa"

print(mydictionary["Francia"])
print(mydictionary)

#modificar valor, se sobreescribe, no hay dos claves iguales
mydictionary["Italia"]="Roma"

print(mydictionary)

#eliminar elemento
del mydictionary["Alemania"]
print(mydictionary)


mydy={"Mosqueteros":3, 23:"Jordan", "Alemania":"Berlin"}
print(mydy)

