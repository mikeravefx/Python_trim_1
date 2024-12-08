# Escribe un programa en Python que:

# Pida al usuario un número entero y lo guarde en una variable

# Pida al usuario otro número entero y lo guarde en otra variable

# Determine cuál de los dos números es mayor y muestre un mensaje indicándolo

# Finalmente, muestre el mayor número

num1 = int(input("Dime un número entero: "))
num2 = int(input("Dime otro número entero: "))

if num1 > num2:
    print("El número 1 es mayor")
else:
    print("El número 2 es mayor")
print(max(num1, num2))  # max devuelve el mayor de dos números  # max(num1, num2)