thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

#Mostrar por consola:

#Mostrar banana

print(thislist[1])

#Eliminar mango

thislist.remove("mango")

print(thislist)

#Buscar el elemento cherry

print(thislist.index("cherry"))

#Indicar con verdadero o falso si el elemento Apple existe

print("Apple" in thislist)

#Añadir pear al final

thislist.append("pear")

print(thislist)

#Añadir mango en el mismo indice en el que estaba antes

thislist.insert(6,"mango")

print(thislist)

#Desde el último elemento hasta el elemento del indice 4 (de atras a delante)

print(thislist[:-4])

#Crear una lista nueva con distintos tipos de elementos y operar entre ella y thislist

thatList = [3, "meat", True, "coke"]

theseList = thislist+thatList

#puedes multiplicar una lista por el numero de elemento de la otra *len(lista)

print(thatList)

print(theseList)