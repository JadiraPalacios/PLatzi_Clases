import threading
import time

def procesar_solicitud(request_id):
    print(f"Procesando solicitud {request_id}")
    time.sleep(3)
    print(f"Solicitud {request_id} completada")

hilos = []
for i in range(3):
    hilo = threading.Thread(target=procesar_solicitud, args=(i,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print("Todas las solicitudes completadas")