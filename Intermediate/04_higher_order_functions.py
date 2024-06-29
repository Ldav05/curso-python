from functools import reduce

### Higher Order Functions ###

# Funciones que hacen cosas con funciones

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_one(first_value, second_value):
    return sum_one(first_value + second_value)

print(sum_two_values_and_one(5, 2))

def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_add_value(5, 2, sum_one))
print(sum_two_values_and_add_value(5, 2, sum_five))

### Closures ###

def sum_ten():
    def add(value):
        return value + 10
    return add
    
add_closure = sum_ten()
print(add_closure(5))

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add
    
add_closure = sum_ten(1)
print(add_closure(5))

sum_ten(5)(1)  # Se puede ejecutar como si fuera una lambda

### Buit-in Higher Order Functions ###

numbers = [2, 3, 5, 10, 21, 30]

# Map

def multiply_two_values(number):
    return number * 2

print(list(map(multiply_two_values, numbers))) # Map nos retorna un objeto lista
print(list(map(lambda number: number * 2, numbers)))  # Usando lambda

# Filter

def filter_greater_than_ten(number):
    if number > 10:
        return True
    else:
        return False

print(list(filter(filter_greater_than_ten, numbers))) # Filter nos retorna un objeto lista
print(list(filter(lambda number: number > 10, numbers))) # Usando lambda

# Reduce

def sum_two_values(first_value, second_value):
    return first_value + second_value

print(reduce(sum_two_values,numbers))
