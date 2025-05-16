numbers={1:"uno",2:"dos",3:"tres"}
print(numbers[2])
information={"Nombre":"Jadira",
             "Apellido":"Palacios",
             "Altura":1.56,
             "Edad":19}
del information["Edad"]
print (information)
claves=information.keys()
#print(type(claves))
values=information.values()
print(values)
pairs=information.items()
print(pairs)
contacts={"Carla":{"Apellido":"Florida",
             "Altura":1.60,
             "Edad":29},
             "JaVier":
             {"Apellido":"Antena",
             "Altura":1.76,
             "Edad":39}}
print(contacts["Carla"])
print(contacts["JaVier"])