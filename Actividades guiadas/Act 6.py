import random
variable1=int(input("introduce un número del 1 al 5:"))
variable2=random.randint(1,5)

if variable1==variable2:
    print("has acertado")
else:
    print("has fallado, el numero es:",variable2)