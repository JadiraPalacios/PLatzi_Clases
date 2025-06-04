def calcular_promedio(numbers):
    """
    Calcula el promedio de una lista de números.

    Parameters:
    numbers (list): Lista de enteros o flotantes.

    Returns:
    float: El promedio de los números en la lista.
    """
    return sum(numbers) / len(numbers)

# Imprime el resultado de la función calcular_promedio
print(calcular_promedio([1, 2, 3, 4, 5]))