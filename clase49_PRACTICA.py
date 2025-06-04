# Lista de empleados
empleados = []

# Función para agregar un empleado
def agregar_empleado(nombre):
    empleados.append(nombre)
    print(f"Empleado '{nombre}' agregado.")

# Función para eliminar un empleado
def eliminar_empleado(nombre):
    if nombre in empleados:
        empleados.remove(nombre)
        print(f"Empleado '{nombre}' eliminado.")
    else:
        print(f"Empleado '{nombre}' no encontrado.")

# Bloque para pruebas
if __name__ == "__main__":
    agregar_empleado("Ana")
    agregar_empleado("Luis")
    print("Lista actual de empleados:", empleados)

    eliminar_empleado("Luis")
    print("Lista actual de empleados:", empleados)

    eliminar_empleado("Carlos")