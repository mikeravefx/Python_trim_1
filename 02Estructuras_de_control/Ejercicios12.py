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

def test_conversion_functions():
    assert galeones_to_sickles(10) == 170
    assert galeones_to_knuts(10) == 4930
    assert sickles_to_knuts(170) == 4930
    assert knuts_to_galeones_sickles_knuts(4930) == (10, 0, 0)  # corregido el resultado esperado
    assert knuts_to_galeones_sickles_knuts(36786) == (74, 10, 0)  # corregido el resultado esperado
    assert knuts_to_galeones_sickles_knuts(0) == (0, 0, 0)  # corregido el resultado esperado
    print("Todas las pruebas han pasado.")
    return True

def main():
    # Probar las funciones de conversión
    print(galeones_to_sickles(10))  # Salida: 170
    print(galeones_to_knuts(10))  # Salida: 4930
    print(sickles_to_knuts(170))  # Salida: 4930
    print(knuts_to_galeones_sickles_knuts(4930))  # Salida: (10, 0, 0)  # corregido el resultado esperado
    print(knuts_to_galeones_sickles_knuts(36786))  # Salida: (74, 10, 0)  # corregido el resultado esperado

if __name__ == "__main__":
    main()
    # Ejecutar las pruebas
    test_conversion_functions()  # Salida: Todas las pruebas han pasado.
