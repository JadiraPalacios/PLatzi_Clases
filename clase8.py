to_do=["Dirigirnos al hotel","Ir a almorar","visital el museo","Volver al hotel"]
print(to_do)
numbers =[1,2,3,4,"cinco"]
print(type(numbers))
mix=["uno",2,3.4,True,[1,2,3]]
print(mix)
print(len(mix))
print("Primer elemento",mix[0])
print("Segundo elemento",mix[1])
print("Ultimo elemento",mix[-1])
string="hola mundo"
print("Primer elemento",string[0])
print("Segundo elemento",string[1])
print("Ultimo elemento",string[-1])
print(mix[0:2])
#añadir esappend
mix.append(False)
print(mix)
mix.append(["a","b"])
print(mix)
#primero mandamos posicion ejempo 1 y luego , e informacion ejemplo ["a","b"]
mix.insert(1,["a","b"])
print(mix)
#index para buscar donde esta lo del parentesis
print(mix.index(["a","b"]))
numbers =[1,2,3,4,90]
print((numbers))
print("Mayor:",max(numbers))
print("Menor:",min(numbers))
del numbers[-2]
print((numbers))
del numbers[:2]
print((numbers))
