# Decoradores

def decorar_saludo(function):
    def decorador():
        print("¡Hola!")
        function()
        print("¡Adios!")

    return decorador

@decorar_saludo
def decir_nombre():
    print("Mi nombre es Santiago")

decir_nombre()

# Decoradores con argumentos

import time

def cronometro(function):

    def decorador(*args, **kwargs):
        inicio = time.time()
        resultado = function(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejeción: {fin - inicio: .4f} segundos")
        return resultado

    return decorador

@cronometro
def suma(a, b):
    time.sleep(1)
    return a + b

print(suma(5, 10))