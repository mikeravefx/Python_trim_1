# Crea un programa en Python que:
# Pida al usuario el radio de una esfera y lo guarde en una variable

# Calcule su área

# Muestre por pantalla el área de la esfera

import math

radio = float(input("Ingrese el radio de la esfera: "))
area = math.pi * radio ** 2
print(area)