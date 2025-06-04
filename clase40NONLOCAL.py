def funcion_externa():
    x = "inicial"

    def funcion_interna():
        nonlocal x
        x = "modificado"
        print("El valor en inner es", x)

    funcion_interna()
    print("El valor afuera es", x)

funcion_externa()