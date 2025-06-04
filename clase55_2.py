import multiprocessing

#funcion que calcule el cuadrado de un numero
def calcular_cuadrado(n):
    return n * n

if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5]

    #crear un pool
    with multiprocessing.Pool() as pool:
        resultados = pool.map(calcular_cuadrado, numeros)
    print(resultados)