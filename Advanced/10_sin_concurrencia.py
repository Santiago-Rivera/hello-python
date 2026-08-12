# Sin concurrencia

import time
import requests

def check_api(api):
    try:
        # Realizamos una petición HTTP GET
        response = requests.get(api, timeout=5)
        if response.status_code == 200:
            print(f"SUCCESS: ¡{api} está en funcionamiento!")
        else:
            print(f"ERROR: ¡{api} respondió con código {response.status_code}!")
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

    # Recorremos y verificamos cada API de forma secuencial
    for api in apis:
        check_api(api)

    elapsed = time.time() - start
    print(f"\n¡Listo! ¡Tomó {elapsed:.4f} segundos!")

if __name__ == '__main__':
    main()