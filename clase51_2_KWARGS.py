def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Llamada a la función con diferentes argumentos
print_info(name="Carlos", age=30, city="Bogotá")
# Salida:
# name: Carlos
# age: 30
# city: Bogotá