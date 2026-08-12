# Multiprocesamiento

import time
import requests
import multiprocessing

# La función se ejecuta en un proceso hijo independiente
def check_api(api, q_compartida):
    try:
        response = requests.get(api, timeout=5)
        if response.status_code == 200:
            # Enviamos el resultado a la cola compartida (se serializa internamente)
            q_compartida.put(f"SUCCESS: ¡{api} está en funcionamiento!")
        else:
            q_compartida.put(f"ERROR: ¡{api} respondió con {response.status_code}!")
    except requests.RequestException:
        q_compartida.put(f"ERROR: ¡{api} está caído!")

# IMPORTANTE: En Windows es obligatorio incluir este bloque
# para evitar que los procesos hijos intenten recrear el programa en un bucle infinito.
if __name__ == '__main__':
    start = time.time()
    
    # Creamos la cola de comunicación especial para procesos
    q = multiprocessing.Queue()

    apis = [
        "https://management.azure.com",
        "https://dev.azure.com",
        "https://api.github.com",
        "https://outlook.office.com/",
        "https://api.somewhereintheinternet.com/",
        "https://graph.microsoft.com",
    ]

    procesos = []
    
    # Creamos e iniciamos un proceso por cada API
    for api in apis:
        proceso = multiprocessing.Process(target=check_api, args=(api, q))
        proceso.start()
        procesos.append(proceso)

    # Leemos los resultados de la cola (operación bloqueante, igual que con hilos)
    for _ in range(len(apis)):
        print(q.get())

    # Esperamos a que todos los procesos hijos finalicen limpiamente
    for proceso in procesos:
        proceso.join()

    elapsed = time.time() - start
    print(f"\n¡Listo! ¡Tomó {elapsed:.4f} segundos!")