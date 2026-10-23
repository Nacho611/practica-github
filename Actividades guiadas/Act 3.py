precio=float(input("introduce el precio:"))

descuento= precio*10/100
salida1=precio-descuento 
iva=salida1*21/100
print("precio con descuento son", salida1, "euros")
print("el IVA es de", iva, "euros")

salida2=salida1+iva
print("el precio final es",salida2,"euros")