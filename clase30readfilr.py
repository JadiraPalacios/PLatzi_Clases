#leer un archivo liena spor linea
"""with open("caperucita.txt","r") as file:
    for lineas in file:
        print(lineas.strip())"""

#leer todas las lineas en una lista
'''with open("caperucita.txt","r") as file:
    lines=file.readlines()
    print(lines)'''

"""with open("caperucita.txt","a") as file:
     file.write("\n\nBy:chatGPT")"""

     #a hace referencia a append

#salto de linea

"""with open("caperucita.txt","w") as file:
   file.write("\n\nBy:chatGPT")"""

# RETO conteo de las lineas del cuento de caperucita
with open ("caperucita.txt", "r") as file:
    lines = file.readlines()
    print(len(lines)) 