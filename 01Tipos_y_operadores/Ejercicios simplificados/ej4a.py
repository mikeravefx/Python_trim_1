# Crea un programa en Python que:

# Pida al usuario su nombre y lo guarde en una variable

# pida al usuario su peso y lo guarde en una variable

# pida al usuario su altura (en m) y lo guarde en una variable

# Calcule el IMC (peso / altura^2) (Índice de masa corporal)

# Muestre por pantalla el nombre y el IMC

nombre = input("Ingrese su nombre: ")
peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))

print(nombre)
print(peso)
print(altura)

imc = peso / (altura ** 2)

print(imc)