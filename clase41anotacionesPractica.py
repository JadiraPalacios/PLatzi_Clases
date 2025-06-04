# Lista de empleados (ejemplo)
empleados = [
    {"nombre": "Ana", "edad": 30, "sueldo": 3000},
    {"nombre": "Luis", "edad": 45, "sueldo": 2500},
    {"nombre": "Marta", "edad": 28, "sueldo": 3200},
    {"nombre": "Carlos", "edad": 40, "sueldo": 2700}
]

# Función que filtra empleados con sueldo mayor al indicado
def empleados_con_sueldo_mayor(lista_empleados, sueldo_minimo):
    return [empleado for empleado in lista_empleados if empleado["sueldo"] > sueldo_minimo]

# Llamada a la función con un sueldo mínimo de ejemplo
sueldo_minimo = 2800
resultado = empleados_con_sueldo_mayor(empleados, sueldo_minimo)

# Mostrar el resultado
print("Empleados con sueldo mayor a", sueldo_minimo)
for emp in resultado:
    print(emp)
