##if solo puede ser verdadera o falsa
##si la condicion es falsa ignora las instrucciones y se las salta
## == igual que
## === estrictamente igual, tipo de variable y valor
## != diferente
#
##cualquier cosa introducida como input es texto, no se puede comparar un int con un str
##funcion int transforma en entero cualquier cosa en un parametro de funcion if
#
#print("Programa evalución notas alumnos")
#
#nota_alumno=input("Introduce nota alumno")
#
#
#def evaluacion (nota):
#    valoracion="aprobado"
#    if nota<5:
#        valoracion="suspenso"
#    return valoracion
#
#print(evaluacion(int(nota_alumno)))
#
#
##if + else: y si no es verdad
#
##else se va a acompañar del if más cercano siempre
#
#print("Verificación de acceso")
#
#edad_usuario=int(input("Introduce tu edad: "))
#
#if edad_usuario<18:
#    print("No puedes pasar")
#elif edad_usuario>100:
#    print("Edad incorrecta")
#else:
#    print("Puedes pasar")
#
#print("EL programa ha finalizado")

#if + elif : se ejecuta else cuando todo lo anterior no se ha cumplido, no solo el if

print("Verificación de acceso")

nota_alumno=int(input("Introduce tu nota: "))

if nota_alumno<5:
    print("Insuficiente")

elif nota_alumno<6:
    print("Suficiente")

elif nota_alumno<7:
    print("Bien")

elif nota_alumno<9:
    print("Notable")

else:
    print("Sobresaliente")

print("El programa ha finalizado")