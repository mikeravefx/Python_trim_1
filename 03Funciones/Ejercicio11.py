
## Ejercicio 11

# Había una vez una tierra próspera y feliz. La gente pagaba impuestos, por supuesto, la felicidad tenía límites. Estos impuestos se pagaban una vez al año segundo los siguientes criterios:
#- Si la persona no cobraba más de 85528 thalers, el impuesto era el 18% de las ganancias menos 556,02 thalers.
#- Si las ganancias eran mayores, el impuesto era 14839,02 thalers sumados a un 32% del exceso de las ganancias por encima de los 85528 thalers.

#Debe aceptar un valor real y mostrar el cálculo del impuesto sin decimales. El gobierno de este país nunca devuelve dinero a sus habitantes, por lo que se el valor del impuesto es negativo, deberá indicar 0.

#|Ganancias|	Impuesto|
#|-|-|
#|10000 thalers|	1244 thalers|
#|100000 thalers|	19470 thalers|
#|1000 thalers|	0 thalers|
#|100 thalers|	0 thalers|
#|10 thalers|	0 thalers|

def calcular_impuesto(ganancias):
    if ganancias <= 85528:
        return 18 * ganancias - 55602
    else:
        return 14839 + 32 * (ganancias - 85528)
ganancias = float(input("Dime la cantidad de ganancias: "))
print(calcular_impuesto(ganancias))  # print(ganancias)  # print(calcular_impuesto(ganancias))
