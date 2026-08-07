# Functions

# Definición

def my_function():
    print("Esto es una función")

my_function()
my_function()
my_function()

# Función con parámetros de entada/argumentos

def sum_two_values(first_value: int, second_vaule):
    print(first_value + second_vaule)

sum_two_values(5, 7)
sum_two_values(5425, 4515)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)

# Función con parámetros de entrada/argumentos y retorno

def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(11, 6)
print(my_result)

# Función con parámetros de entrada/argumentos por clave

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname="Rivera", name="Santiago")

# Función con parámetros de entrada/argumentos por defecto

def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Santiago", "Rivera")
print_name_with_default("Santiago", "Rivera", "Sinsinati")

# Función con parámetros de entrada/argumentos arbitrarios

def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Python", "Sinsinati")
print_upper_texts("Hola")