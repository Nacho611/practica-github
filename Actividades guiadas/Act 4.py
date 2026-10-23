import math
variable_radio=float(input("introduce el valor de radio"))

variable_area=math.pi*(variable_radio**2)
variable_perimetro=2*math.pi*variable_radio
print("el área es:",variable_area)
print("el area es:",variable_perimetro)

#primer método de redondeo
print("el resultado es:",round(variable_area,2))
print("el resultado es: {round(variable_area:.2f)}")
