# Programacion asyncronica

import time
import asyncio
import aiohttp

# Definimos una corutina para verificar una API
async def check_api(session, api):
    try:
        # await cede el control al Event Loop mientras se hace la petición HTTP
        async with session.get(api, timeout=5) as response:
            if response.status == 200:
                return f"SUCCESS: ¡{api} está en funcionamiento!"
            else:
                return f"ERROR: ¡{api} respondió con {response.status}!"
    except Exception:
        return f"ERROR: ¡{api} está caído!"

async def main():
    start = time.time()

    apis = [
        "https://management.azure.com",
        "https://dev.azure.com",
        "https://api.github.com",
        "https://outlook.office.com/",
        "https://api.somewhereintheinternet.com/",
        "https://graph.microsoft.com",
    ]

    # aiohttp requiere manejar las peticiones dentro de una sesión
    async with aiohttp.ClientSession() as session:
        # Creamos una lista de tareas (corutinas listas para ejecutarse)
        tasks = [check_api(session, api) for api in apis]
        
        # asyncio.gather lanza todas las tareas concurrentemente en el Event Loop
        # y espera hasta que todas hayan finalizado para retornar los resultados
        resultados = await asyncio.gather(*tasks)

        for resultado in resultados:
            print(resultado)

    elapsed = time.time() - start
    print(f"\n¡Listo! ¡Tomó {elapsed:.4f} segundos!")

if __name__ == '__main__':
    # Iniciamos el bucle de eventos ejecuntando la corutina principal
    asyncio.run(main())
