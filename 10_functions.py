### Functions ###

def my_function():
    print("Esto es una función")
    
my_function()

def sum_two_values(first_number: int, second_number: int): # Recomendable dejar definido el tipo de dato para mejor legibilidad (Opinión propia)
    print(first_number + second_number)
    
sum_two_values(2,3)
sum_two_values(34253, 5654)
sum_two_values("2", "3")
sum_two_values(1.4, 5.2)

# Función con retorno

def sum_two_values_with_return(first_number: int, second_number: int):
    my_sum = first_number + second_number
    return my_sum

my_result = sum_two_values_with_return(8, 2)
print(my_result)

def print_name(name, surname):
    print(f"{name} {surname}") # Formatearlo como string
    
print_name("Luis", "Gordon")
print_name(surname = "Gordon", name = "Luis") # Se le puede cambiar el orden

# Definir un valor por defecto

def print_name_with_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")
    
print_name_with_default("Luis", "Gordon")   
print_name_with_default("Luis", "Gordon", "Luka")

# Número de parámetros dinámicos

def print_texts(*texts):
    for text in texts: # Se puede manejar como a una lista
        print(text)
    
print_texts("Hola", "Python", "Luka")

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())
    
print_upper_texts("Hola", "Python", "Luka")

