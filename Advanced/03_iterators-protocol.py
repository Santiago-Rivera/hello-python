mi_lista = [10, 20, 30] # Esto es un ITERABLE (el libro)

mi_marcapaginas = iter(mi_lista) # Obtenemos el ITERADOR

print(next(mi_marcapaginas)) # Imprime: 10
print(next(mi_marcapaginas)) # Imprime: 20
print(next(mi_marcapaginas)) # Imprime: 30

# Iteradores

class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.actual = 1 # Aquí empezamos a contar
    
    # Regla 1: El método __iter__
    def __iter__(self):
        # Como esta misma clase va a llevar la cuenta, 
        # devolvemos "self" (ella misma es el marcapáginas)
        return self
    
    # Regla 2: El método __next__
    def __next__(self):
        # Comprobamos si ya llegamos al límite
        if self.actual > self.limite:
            raise StopIteration # ¡Avisamos que terminamos!
        
        # Guardamos el número actual para devolverlo luego
        numero_a_devolver = self.actual
        
        # Preparamos el siguiente número para la próxima vez
        self.actual += 1
        
        return numero_a_devolver

# --- ¡Vamos a probarlo! ---

mi_contador = Contador(3)

# Como seguimos el protocolo, ¡Python sabe usarlo en un for!
for numero in mi_contador:
    print(numero)

# Salida:
# 1
# 2
# 3
