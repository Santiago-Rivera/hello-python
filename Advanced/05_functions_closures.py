# Clausuras

def crear_multiplicador(n):
    
    def multiplicar(x):
        return x * n
    
    return multiplicar

multiplicar_por_2 = crear_multiplicador(2)
multiplicar_por_5 = crear_multiplicador(5)

print(multiplicar_por_2(10))
print(multiplicar_por_5(10))