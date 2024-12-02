def cadena_invertida(cadena: str) -> str:
    """
    Devuelve la cadena invertida.

    Esta función toma una cadena de texto y devuelve una nueva cadena con los caracteres 
    en orden inverso.

    Args:
        cadena (str): La cadena a invertir.

    Returns:
        str: La cadena invertida.

    Ejemplos:
    >>> cadena_invertida("hola")
    'aloh'
    >>> cadena_invertida("python")
    'nohtyp'
    >>> cadena_invertida("12345")
    '54321'
    >>> cadena_invertida("")
    ''
    """
    return cadena[::-1]

def eliminar_espacios_y_puntuacion(cadena: str) -> str:
    """
    Elimina los espacios y los signos de puntuación de una cadena de texto.

    Esta función toma una cadena de texto y devuelve una nueva cadena en la que se han 
    eliminado todos los espacios y los caracteres de puntuación, dejando solo las letras.

    Args:
        cadena (str): La cadena de texto de entrada.

    Returns:
        str: La cadena sin espacios ni puntuación.

    Ejemplos:
    >>> eliminar_espacios_y_puntuacion("Hola cómo estás")
    'Holacómoestás'
    >>> eliminar_espacios_y_puntuacion("Hola, ¿cómo estás?")
    'Holacómoestás'
    >>> eliminar_espacios_y_puntuacion("Python es genial.")
    'Pythonesgenial'
    >>> eliminar_espacios_y_puntuacion("¡Bienvenido!")
    'Bienvenido'
    >>> eliminar_espacios_y_puntuacion("!#$%&/()=><")
    ''
    >>> eliminar_espacios_y_puntuacion("   ")
    ''
    """
    resultado = ""
    for letra in cadena:
        if not letra.isspace() and letra.isalpha():
            resultado += letra
    return resultado
    # return cadena.replace(" ", "")

def es_palindromo(cadena: str) -> bool:
    """
    Determina si una cadena es un palíndromo.

    Un palíndromo es una palabra, frase o número que se lee igual de izquierda a derecha 
    que de derecha a izquierda (ignorando los espacios y la puntuación en el caso de las frases).

    Args:
        cadena (str): La cadena a verificar.

    Returns:
        bool: `True` si la cadena es un palíndromo, `False` en caso contrario.

    Ejemplos:
    >>> es_palindromo("ana")
    True
    >>> es_palindromo("reconocer")
    True
    >>> es_palindromo("python")
    False
    >>> es_palindromo("a man a plan a canal panama")
    True
    """
    # return eliminar_espacios_y_puntuacion(cadena) == cadena_invertida(eliminar_espacios_y_puntuacion(cadena))
    cadena_solo_letras = eliminar_espacios_y_puntuacion(cadena)
    cadena_reves = cadena_invertida(cadena_solo_letras)
    cadena_reves_solo_letras = eliminar_espacios_y_puntuacion(cadena_reves)
    return cadena_solo_letras == cadena_reves_solo_letras


print(es_palindromo("a man a plan a canal panama"))