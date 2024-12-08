## Ejercicio 2
# Crea una función que reciba una cadena e indique si se trata de un verbo en infinitivo.
# Vamos a considerar verbos todas aquellas palabras que terminen en -ar, -er, -ir.
cadena = ["ser", "estar", "querer"]
def recibiracadena(cadena: list[str])-> bool:
    arreglo=[]
    for longitud in range (len(cadena)):
        while opcion !="S":
            if cadena[longitud].endswith("ar") or cadena[longitud].endswith("er") or cadena[longitud].endswith("ir"):
                arreglo.append(longitud)
                opcion = input("¿Desea ingresar otra cadena S/N?")
                if opcion == "N":
                    print("No es un verbo en infinitivo")
                    return False
            else:
                opcion = input("¿Desea ingresar otra cadena S/N?")
                if opcion == "N":
                    print("No es un verbo en infinitivo")
                    return False

    recibiracadena(cadena)
    print(arreglo)
    print(cadena)

