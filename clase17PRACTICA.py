print("NUMEROS IMPARES MENORES A 20")
def fibonacci(limit): 
    a= 1 
    while a<limit: 
        yield a 
        a = a+2
for num in fibonacci (20): 
    print(num)


print("NUMEROS PARES MENORES A 20")

def fibonacci(limit): 
    a= 0 
    while a<limit: 
        yield a 
        a = a+2
for num in fibonacci (20): 
    print(num)