## Ejercicio 12

# Crea una calculadora del mundo mágico de Harry Potter, que convirta galeones, sickels y knuts. Debe ofrecer inicialmente un menú en el que se indiquen las siguientes opciones:
#- Conversión de galeones a sickels.
#- Conversión de galeones a knuts.
#- Conversión de sickles a knuts.
#- Conversión de knuts a galeones, sickles y knuts (mínimo número de monedas posibles).

#Recuerda que:
#- 1 galeón = 17 sickles
#- 1 sickle = 29 knuts

#**DATOS DE PRUEBA**
#|Galeones|Sickles|Knuts|
#|-|-|-|
#|10 galeones|170 sickles|4930knuts|
#|45 galeones|765 sickles|22185knuts|

#Opción 4

#|knuts|galeones, sicles, knuts|
#|-|-|
#|1000 knuts|2 galeones, 0 sickles y 14 knuts|
#|36786 knuts|74 galeones,  10 sickles y 14 knuts|


def galeones_to_sickles(galeones):
    return galeones * 17

def galeones_to_knuts(galeones):
    return galeones * 17 * 29

def sickles_to_knuts(sickles):
    return sickles * 29

def knuts_to_galeones_sickles_knuts(knuts):
    galeones = knuts // (17 * 29)
    remaining_knuts = knuts % (17 * 29)
    sickles = remaining_knuts // 29
    remaining_knuts = remaining_knuts % 29
    return galeones, sickles, remaining_knuts

def main():
    # Test the conversion functions
    print(galeones_to_sickles(10))  # Output: 170
    print(galeones_to_knuts(10))  # Output: 4930
    print(sickles_to_knuts(170))  # Output: 4930
    print(knuts_to_galeones_sickles_knuts(4930))  # Output: (10, 0, 14)
    print(knuts_to_galeones_sickles_knuts(36786))  # Output: (74, 10, 14)

if __name__ == "__main__":
    main()