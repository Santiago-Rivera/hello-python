# Error Types

# SyntaxError

#print "¡Hola comunidad!" # Descomenta para Error
from math import pi
import math
print("¡Hola comunidad!")

# NameError

language = "Spanish" # Comentar para Error
print(language)

# IndexError

my_list = ["Python", "Bash", "Kotlin", "Dart", "Java"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
# print(my_list[5]) # Descomnetar para Error

# ModuleNotFoundError

#import maths # Descomentar para Error

# AtributeError

# print(math.PI) # Descomentar para Error
print(math.pi)

# KeyError

my_dict = {"Nombre": "Santiago", "Apellido": "Rivera", "Edad": 21, 1: "Python"}
print(my_dict["Edad"])
# print(my_dict["Apelido"]) # Descomentar para Error
print(my_dict["Apellido"])

# TypeError

# print(my_list["0"]) # Descomentar para Error
print(my_list[0])
print(my_list[False])

# ImportError

#from math import PI # Descomentar parar Error
print(pi)

# ValueError

# my_int = int("10 años") # Descomentar para Error
my_int = int("10")
print(type(my_int))

# ZeroDivisionError

# print(4/0) # Descomentar para Error
print(4/2)