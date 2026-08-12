# Multithreading

import time
import requests
import threading

def check_api(api):
    try:
        response = requests.get(api, timeout=5)
        if response.status_code == 200:
            print(f"SUCCESS: ¡{api} está en funcionamiento!")
        else:
            print(f"ERROR: ¡{api} respondió con {response.status_code}!")
    except requests.RequestException:
        print(f"ERROR: ¡{api} está caído!")

def main():
    start = time.time()

    apis = [
        "https://management.azure.com",
        "https://dev.azure.com",
        "https://api.github.com",
        "https://outlook.office.com/",
        "https://api.somewhereintheinternet.com/",
        "https://graph.microsoft.com",
    ]

    # Recorremos e iniciamos un hilo por cada API
    for api in apis:
        hilo = threading.Thread(target=check_api, args=(api,))
        hilo.start()

    elapsed = time.time() - start
    print(f"¡Listo! ¡Tomó {elapsed:.6f} segundos!")

if __name__ == '__main__':
    main()

import time
import requests
import threading
import queue

# La función ahora recibe la cola como parámetro
def check_api(api, q):
    try:
        response = requests.get(api, timeout=5)
        if response.status_code == 200:
            q.put(f"SUCCESS: ¡{api} está en funcionamiento!")
        else:
            q.put(f"ERROR: ¡{api} respondió con {response.status_code}!")
    except requests.RequestException:
        q.put(f"ERROR: ¡{api} está caído!")

def main():
    start = time.time()
    
    # Creamos una cola segura
    q = queue.Queue()

    apis = [
        "https://management.azure.com",
        "https://dev.azure.com",
        "https://api.github.com",
        "https://outlook.office.com/",
        "https://api.somewhereintheinternet.com/",
        "https://graph.microsoft.com",
    ]

    for api in apis:
        # Pasamos la cola como argumento a cada hilo
        hilo = threading.Thread(target=check_api, args=(api, q))
        hilo.start()

    # Leemos SOLO UN DATO de la cola
    print(q.get())

    elapsed = time.time() - start
    print(f"\n¡Listo! ¡Tomó {elapsed:.4f} segundos!")

if __name__ == '__main__':
    main()

# Si tenemos 6 APIs, pero intentamos leer 7 veces de la cola:
# print(q.get()) # 1
# print(q.get()) # 2
# print(q.get()) # 3
# print(q.get()) # 4
# print(q.get()) # 5
# print(q.get()) # 6
#
# print(q.get()) # 7 -> Bloqueo eterno (el programa se congela aquí)
#
# Leemos de la cola exactamente una vez por cada API
# for _ in range(len(apis)):
#     print(q.get())