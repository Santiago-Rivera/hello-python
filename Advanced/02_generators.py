lista_cuadrados = [x**2 for x in range(100)]
suma_total = sum(lista_cuadrados)
print(suma_total)
print(lista_cuadrados)

# Generadores

gen_cuadrados = (x**2 for x in range(100))
suma_total = sum(gen_cuadrados)
print(suma_total)
print(gen_cuadrados)
for x in gen_cuadrados: print(x)
