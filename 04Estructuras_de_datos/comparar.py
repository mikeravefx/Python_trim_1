lista = [1, 2, 3, 4, 5]
lista2 =[1,2,2,3,3,3,4,4,4,5,5,5]

total =set()
for i in range(len(lista)):
    for j in range(len(lista2)):
        if lista[i] == lista2[j]:
            print(f"El elemento {i} es igual a {j}")         
            total.add(lista2[j])
print(total)

