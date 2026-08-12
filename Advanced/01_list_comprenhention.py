# Alamacena cuadrados de un rango de números

cuadrados = []

for x in range(1, 6):
    cuadrados.append(x**2)
print(cuadrados)

cuadrados = [x**2 for x in range(1,6)]
print(cuadrados)

numeros = [1,2,3,4,5,6,7,8,9,10]

pares = []

for x in numeros:
    if x % 2 == 0:
        pares.append(x)
print(pares)

pares = [x for x in numeros if x % 2 == 0]
print(pares)