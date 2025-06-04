x = "global"  # Variable global

#funcion externa
def funcion_externa():
    x = "externa"  # Redefine 'x' en el ámbito de la función externa

    #funcion interna
    def funcion_interna():
        x = "local"  # Redefine 'x' en el ámbito de la función interna
        print(x)

    funcion_interna()
    print(x)

funcion_externa()
print(x)