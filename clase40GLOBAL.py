x=5#Variable Global

def modify_global():
    global x
    x+=3
    print(f"Valor Modificado: {{x}}")

modify_global()
print(x)