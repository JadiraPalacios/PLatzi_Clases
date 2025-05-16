
movimientos=[1,2,3]
print("  ")
print("BIENVEIDO AL JUEGO")
print("  ")
print("Una indicacion de este juego es que:")
print("  ")

print("1=PIEDRA"+"  "
      "2=PAPEL"+"  "
      "3=TIJERA")
print("  ")

J1=int(input("JUGADOR 1 Ingresa Eleccion: "))


J2=int(input("JUGADOR 2 Ingresa Eleccion: "))


if J1==1 and J2==1:
    print("  ")
    print("PIEDRA  VS  PIEDRA")
    print("  ")
    print("ES UN EMPATE NADIE GANA!!")
    print("  ")

if J1==1 and J2==2:
    print("  ")
    print("PIEDRA  VS  PAPEL")
    print("  ")
    print("GANA PAPEL")
    print("GANA JUGADOR 2!!")
    print("  ")

if J1==1 and J2==3:
    print("  ")
    print("PIEDRA  VS  TIJERA")
    print("  ")
    print("GANA PIEDRA")
    print("GANA JUGADOR 1!!")
    print("  ")


if J1==2 and J2==2:
    print("  ")
    print("PAPEL  VS  PAPEL")
    print("ES UN EMPATE NADIE GANA!!")
    print("  ")

if J1==2 and J2==3:
    print("  ")
    print("PAPEL  VS  TIJERA")
    print("  ")
    print("GANA TIJERA")
    print("GANA JUGADOR 2!!")
    print("  ")

if J1==2 and J2==1:
    print("  ")
    print("PAPEL  VS  PIEDRA")
    print("  ")
    print("GANA PAPEL")
    print("GANA JUGADOR 1!!")
    print("  ")

###
if J1==3 and J2==3:
    print("  ")
    print("TIJERA  VS  TIJERA")
    print("  ")
    print("ES UN EMPATE NADIE GANA!!")
    print("  ")

if J1==3 and J2==2:
    print("  ")
    print("TIJERA  VS  PAPEL")
    print("  ")
    print("GANA TIJERA")

    print("GANA JUGADOR 1!!")
    print("  ")

if J1==3 and J2==1:
    print("  ")
    print("TIJERA  VS  PIEDRA")
    print("  ")
    print("GANA PIEDRA")
    print("GANA JUGADOR 2!!")
    print("  ")

exit()









