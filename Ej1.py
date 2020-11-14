print("Ejercicio 1")
print("""1 
2 
3\n""")

print("Lo siguiente escribirlo como una función")
def ejercicio(): 
    print("1")
    print("2")
    print("3")

ejercicio()
ejercicio()
ejercicio()
print(" ")
print("Escribirlo usando variables\n")

a=1
b=2
suma=a+b
print("Suma: " + str(a)  + " + " + str(b) + " = " + str(suma))

print(" ")

print("Escribirlo usando una función\n")

def suma(a,b):
        return "El resultado de %i y %i es: %i" % (a,b,a+b)

print (suma (4,9))
