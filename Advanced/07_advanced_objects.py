# Objetos Avanzados

class ConfiguracionDinamica():
    def __init__(self):
        self.configuraciones_base = {"tema": "oscuro", "idioma": "es"}
        self.datos = {"Esto es un dato importante"}

    def __getattr__(self, name):
        if name in self.configuraciones_base:
            return self.configuraciones_base[name]
        else:
            return f"El atributo '{name}' no existe en la configuración."

config = ConfiguracionDinamica()
print(config.datos)
print(config.tema)
print(config.version)

class UsuarioEstricto:
    def __setattr__(self, nombre, valor):
        if nombre == "edad":
            if not isinstance(valor, int) or valor < 0:
                raise ValueError("La edad debe ser un número entero positivo")

        self.__dict__[nombre] = valor

usuario = UsuarioEstricto()
usuario.nombre = "Santiago"
usuario.edad = -5