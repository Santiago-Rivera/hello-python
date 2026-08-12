class MetaclaseMayusculas(type):
    # El método __new__ es el que realmente "construye" la clase en memoria
    def __new__(cls, nombre_clase, bases, diccionario_clase):
        
        diccionario_nuevo = {}
        # Iteramos sobre todos los atributos/métodos definidos en la clase
        for nombre_atributo, valor in diccionario_clase.items():
            # Si no es un método mágico (no empieza con __), lo forzamos a mayúsculas
            if not nombre_atributo.startswith('__'):
                diccionario_nuevo[nombre_atributo.upper()] = valor
            else:
                diccionario_nuevo[nombre_atributo] = valor
                
        # Llamamos al 'type' original para que termine de crear la clase con nuestro nuevo diccionario
        return super().__new__(cls, nombre_clase, bases, diccionario_nuevo)

# 2. Usamos la Metaclase en una clase normal usando (metaclass=...)
class MiClase(metaclass=MetaclaseMayusculas):
    def saludar(self):
        return "Hola!"
        
    def despedirse(self):
        return "Adiós!"

# --- Probando la magia ---

objeto = MiClase()

# ¡Magia! Los métodos originales en minúscula NO existen
# objeto.saludar() # Esto daría un AttributeError

# La Metaclase interceptó la creación y los convirtió a mayúsculas
print(objeto.SALUDAR())    # Imprime: Hola!
print(objeto.DESPEDIRSE()) # Imprime: Adiós!