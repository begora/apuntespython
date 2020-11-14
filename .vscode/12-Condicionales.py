#edad=7
#
#if 0<edad<100:
#    print("Edad correcta")
#else:
#    print("Edad incorrecta")
    
salario_presi=int(input("Introduce salario presidente "))
print("Salario presidente: " + str(salario_presi))

salario_director=int(input("Introduce salario director "))
print("Salario director: " + str(salario_director))

salario_jefe=int(input("Introduce salario jefe "))
print("Salario jefe: " + str(salario_jefe))

salario_admin=int(input("Introduce salario admin "))
print("Salario admin: " + str(salario_admin))

if salario_admin<salario_jefe<salario_director<salario_presi:
    print("Todo funciona")
else:
    print("Algo falla")

    