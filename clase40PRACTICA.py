import json

def cargar_empleados_desde_json(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

def filtrar_empleados_por_sueldo(empleados, sueldo_minimo):
    return [empleado for empleado in empleados if empleado["salary"] > sueldo_minimo]

# Ejemplo de uso:
if __name__ == "__main__":
    ruta = "clase40.json"  # Asegúrate de que este archivo exista
    sueldo_minimo = 2800

    empleados = cargar_empleados_desde_json(ruta)
    empleados_filtrados = filtrar_empleados_por_sueldo(empleados, sueldo_minimo)

    print("Empleados que ganan más de", sueldo_minimo, ":")
    for emp in empleados_filtrados:
        print(emp)
