# Escribe un programa qen Python que:

# Pida al usuario un número entero y lo guarde en una variable

# Muestre un mensaje indicando si el número es par o impar

# Si el número es impar, muestre un mensaje indicando que el número es impar

# Si el número es par, muestre un mensaje indicando que el número es par

# Finalmente, muestre el número original

n = int(input("Dime un número entero: "))

if n % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
print(n)