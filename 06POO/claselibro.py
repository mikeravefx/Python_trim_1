# Ejercicios

# Ejercicio 1:
# Crea una clase llamada `Libro` que guarde la información de cada uno de los libros de una biblioteca. La clase debe guardar el título del libro, autor, número de ejemplares del libro y el número de ejemplares prestados. La clase contendrá los siguientes métodos:
# 	Constructor.
# -	Método `prestar()` que incremente el atributo correspondiente cada vez que se realice un préstamo del libro. No se podrán prestar libros de los que no queden ejemplares disponibles para prestar. Devolverá `True` si se pudo realizar la operación y `False` en caso contrario.
# -	Método `devolver()` que decremente el atributo correspondiente cuando se produzca la devolución de un libro. No se podrán devolver libros que no se habían prestado. Devuelve `True` si se pudo realizar la operación y `False`, en caso contrario.

# #Prueba el funcionamiento de la clase `Libro` desde el programa principal.

# Ejercicio 2:
# Crea una clase llamada `Rectangulo` que:
# - Declare atributos para la base y la altura de un rectángulo.
# - Declare un constructor. Por defecto, el rectángulo tendrá una base de 0 y una altura de 0.
# - Declare los siguientes métodos:
#   - `area()`: devuelve el área del rectángulo.
#   - `__str__`:# devuelve una cadena conteniendo su área y altura.
#   - `es_cuadrado()`: devuelve un booleano indicando si el rectángulo es cuadrado.
#Prueba el funcionamiento de la clase Rectangulo desde el programa principal.

from typing import Dict

# Diccionario para almacenar los libros
libros: Dict[str, Dict[str, int]] = {}

def agregar_libro(titulo: str, autor: str, num_ejemplares: int) -> None:
    libros[titulo] = {'autor': autor, 'num_ejemplares': num_ejemplares, 'num_prestados': 0}

def prestar_libro(titulo: str) -> bool:
    if titulo in libros and libros[titulo]['num_prestados'] < libros[titulo]['num_ejemplares']:
        libros[titulo]['num_prestados'] += 1
        return True
    return False

def devolver_libro(titulo: str) -> bool:
    if titulo in libros and libros[titulo]['num_prestados'] > 0:
        libros[titulo]['num_prestados'] -= 1
        return True
    return False

# Pruebas
agregar_libro("Cien años de soledad", "Gabriel García Márquez", 5)
print(f"Préstamo realizado: {prestar_libro('Cien años de soledad')}")  # Debería devolver True
print(f"Préstamo realizado: {prestar_libro('Cien años de soledad')}")  # Debería devolver True
print(f"Devolución realizada: {devolver_libro('Cien años de soledad')}")  # Debería devolver True
print(f"Devolución realizada: {devolver_libro('Cien años de soledad')}")  # Debería devolver True
print(f"Devolución realizada: {devolver_libro('Cien años de soledad')}")  # Debería devolver False
