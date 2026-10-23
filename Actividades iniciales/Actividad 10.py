'''Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar.'''
'''Te muestra el cociente, el resto y si es par o impar'''
variable1=float(input("introduce el primer número:"))
variable2=float(input("introduce el segundo número:"))
print("el cociente es:",variable1/variable2)
print("el resto es:",variable1%variable2)
if variable1 % 2==0:
    print("el dividendo es par")
else:
    print("el dividendo es impar")