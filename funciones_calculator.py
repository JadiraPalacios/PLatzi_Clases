
def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def producto(a,b):
    return a * b

def division(a,b):
    if b == 0:
        print('Error: No se puede dividir por 0')
    else:
        return a / b

print(" ")
def calculadora():
    while True:

        print('Seleccione una opción del 1 al 5:')
        print(" ")
        print('1. Suma')
        print('2. Resta')
        print('3. Producto')
        print('4. Division')
        print('5. Salir')

        print(" ")
        try:
            opcion = int(input('Ingrese la opción elegida: '))
        except:
            print(" ")
            print('Entrada no válida, por favor ingrese un valor entre 1 y 5')
            print(" ")
            continue

        if opcion == 5:
            print(" ")
            print('Saliendo de la calculadora')
            print(" ")
            break

        if opcion in [1,2,3,4]:
            try:
                print(" ")
                num1 = float(input('Ingrese el primer número: '))
               
                num2 = float(input('Ingrese el segundo número: '))
            except:
                print(" ")
                print('Entrada no válida. Por favor ingrese números válidos.')
                print(" ")
                continue

            if opcion == 1:
                print(" ")
                print(f'{num1} + {num2} = ', suma(num1,num2))
                print(" ")
            elif opcion ==2:
                print(" ")
                print(f'{num1} - {num2} = ', resta(num1,num2))
                print(" ")
            elif opcion == 3:
                print(" ")
                print(f'{num1} * {num2} = ', producto(num1,num2))
                print(" ")
            elif opcion == 4:
                print(" ")
                print(f'{num1} / {num2} = ', division(num1,num2))
                print(" ")
        else:
            print(" ")
            print('No es una opción valida. Intente nuevamente por favor')
            print(" ")

calculadora()