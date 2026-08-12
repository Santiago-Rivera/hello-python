palabras = ["sol", "murcielago", "luz", "computadora"]

def mas_de_5_letras(palabra):
    return len(palabra) > 5

resultados = filter(mas_de_5_letras, palabras)
print(list(resultados))

# Funciones lambdas

resultados = filter(lambda palabra: len(palabra) > 5, palabras)
print(list(resultados))