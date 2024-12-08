# Escribe un programa en Python que:

# Pida al usuario un número entero y lo guarde en una variable

# Indique si el número es par, impar o cero y muestre un mensaje indicandolo

# Finalmente, muestre el número original

n = int(input("Dime un número entero: "))

if n % 2 == 0:
    print("El número es par")
elif n % 2 == 1:
    print("El número es impar")
else:
    print("El número es cero")
print(n)

