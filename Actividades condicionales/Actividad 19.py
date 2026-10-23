''' Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son 
iguales '''
variable1=float(input("introduce el primer número:"))
variable2=float(input("introduce el segundo número:"))
if variable1>variable2:
    print (f"el numero {variable1} es mayor que el número {variable2}")
else:
    print (f"el numero {variable2} es mayor que el número {variable1}")
if variable1==variable2:
    print (f"el numero {variable1} es igual que el número {variable2}")