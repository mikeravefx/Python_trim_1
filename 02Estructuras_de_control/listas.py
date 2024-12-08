from typing import List

def recorrer_listas(lista: List[int], lista1: List[int]) -> List[int]:
    # Function body goes here
    resultado = []
    for i in range(len(lista)):
        resultado.append(lista[i] + lista1[i])
    return resultado

lista = [1, 2, 3, 4, 5]
lista1 = [6, 7, 8, 9, 10]

resultado = recorrer_listas(lista, lista1)
print(resultado)
