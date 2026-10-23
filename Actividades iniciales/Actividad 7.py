'''programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes forzar que el resultado de la división tenga 2 decimales?'''
'''que te pida dos números y te haga las siete opreaciones posibles.'''
variable1=int(input("introduce el primer número:"))
variable2=int(input("introduce el segundo número:"))
división=variable1/variable2

print("la suma es:",variable1+variable2)
print("la resta es:",variable1-variable2)
print("el producto es:",variable1*variable2)
print("la división es:",round(división,2))
print("el cociente de la división:",variable1//variable2)
print("el resto de la división:",variable1%variable2)
print("la potencia es:",variable1**variable2)
