#tuplas: inmutables, no se pueden modificar despues de la creacion
#se puede extraer porcion como nueva tupla
#se puede comprobar si hay un elemento
#clave diccionario
#metodo index busqqueda

miTupla=("raquel",34,45,"raquel")
print(miTupla)
#se pueden omitir los parentesis
#comienzan posición 0

#indice qué elemnto
print(miTupla[2])

milist=list(miTupla) #creas una lista con los mismos elementos de la tupla

print(milist)

#convertir lista en tupla
milist1=["raquel","kiko"]
miTupla2=tuple(milist1)

print(miTupla2)

print("Juan" in miTupla)

#metodo count. cuantos elementos

print(miTupla.count("raquel"))

#metodo len (longitud una tupla, cuantos elementos en general)

print(len(miTupla))

#tuplas unitarias -  necesita una , 

mitupla3=("rosa,")
print(len(mitupla3))

# empaquetado 

# #desempaquetado , asignar valor tupla a una variable

sutupla=("raquel", 18, 7, 95)
nombre, dia, mes, agno=sutupla
print(nombre)
print(agno)


