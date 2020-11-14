# Sintaxis lista : nombreLista=[elem1,elem2...]
# cuando "llamas" empieza a contar desde el 0
# pueden almacenar distintos tipos de datos, enteros, texto, boleano...
miLista=["María", "Pepe", "Marta", "Antonio"]

# [:] para llamar la lista entera

print(miLista[:]) 

# [0] para llamar un elemento

print(miLista[0])

# -2 empieza a contar desde el final -1

print(miLista[-2]) 

#Porción de lista (de tal indice (incluido) a tal indice (excluido))

print(miLista[0:3])

# los dos primeros (0,1 - deja exlcuido desde 2)

print(miLista[:2]) 

# los dos últimos desde 2 incluido(3)

print(miLista[2:]) 

#agrega elemento final lista

miLista.append("Sandra") 

print(miLista[:])

# incluir elemento en una posición concreta

miLista.insert(2,"Pedro") 

print(miLista[:])

#incluir varios elementos al final de la lista / concatenar dos listas

miLista.extend(["Ana","Raquel","Lucia"]) 

print(miLista[:])

# saber en qué posición de la lista se encuentra un elemento

print(miLista.index("Antonio")) 

#si hay dos elementos con el mismo nombre siempre te va a dar la posición del primer elemento

# preguntar si se encuentra o no en la lista true/false

print("Pepe" in miLista) 

#elimar elemento

miLista.remove("Ana")

print(miLista[:])

#elimar ultimo elemento lista

miLista.pop()

#sumar listas diferentes
#cuando se trabaja listas, el operador + hace de concatenador


miLista2=[3,8,9,23]

miLista3=miLista+miLista2

print(miLista3)


#operador * funciona modo de repetidor dentro de una misma lista

miLista4=[2,5,7,9]*4

print(miLista4)

# operador * puedes crear una lista nueva para no modificar la original y poder seguir trabajando con ella

miLista5=miLista*2

print(miLista5)


