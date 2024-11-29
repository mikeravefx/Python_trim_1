import random

matriz = []

for num_fila in range(6):
    lista_fila = []
    for num_columna in range(7):
        valor = random.randint(0, 9)
        lista_fila.append(valor)
    matriz.append(lista_fila)  

print(matriz)  