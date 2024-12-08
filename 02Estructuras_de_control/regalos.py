from typing import List

def agregar_a_lista() -> List[str]:
    lista: List[str] = []  # Inicializar lista vacía
    while True:
        try:
            # Solicitar entrada de datos
            elemento: str = input("Introduce un elemento para agregar a la lista (o 'salir' para terminar): ")
            
            # Verificar si el usuario desea salir
            if elemento.lower() == 'salir':
                break
            
            # Agregar el elemento a la lista
            lista.append(elemento)
            print(f"Elemento agregado. Lista actual: {lista}")
        
        except ValueError as e:
            print(f"Error: {e}. Por favor, introduce un valor válido.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
    
    print(f"Lista final: {lista}")
    return lista

# Llamar a la función
mi_lista: List[str] = agregar_a_lista()