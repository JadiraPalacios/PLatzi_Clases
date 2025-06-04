def log_employee_action(func):
    def wrapper(empleada):
        if empleada.get("role") == "Trabanjando":
            return func(empleada)
        else:
            print(f"La Empleada {empleada['name']} está {empleada['role']}")
    return wrapper

@log_employee_action
def accion_de_empleada(empleada):
    print(f"La Empleada {empleada['name']} está Trabajando")

# Lista de empleadas
empleadas = [
    {"name": "Carla", "role": "Rompiendo"},
    {"name": "Mia", "role": "Desordenando"},
    {"name": "Ana", "role": "llendose"},
    {"name": "Carla", "role": "Trabanjando"},
    {"name": "Jamin", "role": "Comiendo"},
    {"name": "Rosa", "role": "Descansando"}
]

# Ejecutar para todas las empleadas
for empleada in empleadas:
    accion_de_empleada(empleada)
