x=100#variable de tipo global
#VARIABLES LOCALES

def funcion_local():
    x = 10  # Variable local
    print("El valor de la variable es", x)


def show_global():
    print(f"El valor de la variable global es {x}")

funcion_local()

#no puedes tener el valor de x fuera de la definicion funcion_local
print(x)