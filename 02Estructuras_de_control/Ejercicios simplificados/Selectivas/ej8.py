# Escribe un programa en Python que:

# Pida una nota en número y devuelva la calificación correspondiente

# Menor que 5: Suspenso

# Entre 5 y 6: Aprobado

# Entre 6 y 7: Bien

# Entre 7 y 9: Notable

# Mayor o igual que 9: Sobresaliente

# Finalmente, muestre el resultado

def clasificar_nota(nota):
    if nota < 5:
        return "Suspenso"
    elif nota < 6:
        return "Aprobado"
    elif nota < 7:
        return "Bien"
    elif nota < 9:
        return "Notable"
    else:
        return "Sobresaliente"

# Pedir la nota al usuario
nota = float(input("Dime una nota: "))

# Obtener la clasificación
clasificacion = clasificar_nota(nota)

# Mostrar el resultado
print(f"Nota: {nota}")
print(f"Clasificación: {clasificacion}")