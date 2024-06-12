# Variables

my_string_variable = "My string variable"  # Es recomendable definir las variables usando snake_case
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable) # str transforma nuestra variable a string (str)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable) 
print("Este es el valor de:",my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Luis", "Gordon", "Luka", 23
print("Me llamo:", name, surname,". Mi edad es:", age, ". Y mi alias es:", alias)

# Inputs
name = input('What is your name: ')
age = input('How older are you: ')

print(name)
print(age)

# Cambiar tipo de dato

name = 23
age = "Luis"
print(name)
print(age)

# ¿Forzamos el tipo? No
address: str = "Mi dirección"
address = 32
address = True
address = 5
address = 1.5
print(address)