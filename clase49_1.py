def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("El divisor no puede ser cero.")
    return a / b
"""print(sumar(2, 4))
print(restar(2, 4))
print(multiplicar(2, 4))
print(dividir(2, 4))"""

if __name__=="__main__":
    print("Operaciones")
    res_1=sumar(3, 4)
    print(f"Suma:{res_1}")
    print(dividir(10, 7))