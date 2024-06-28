### Tuples ###

# Las tuplas no son mutables

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (22, 1.87, "Luis", "Gordon", "Luis")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Luis")) # Cuenta el cuantas veces está el elemento
print(my_tuple.index("Luis")) # Devuelve el indice del elemento
print(my_tuple.index("Gordon"))

#my_tuple[1] = 1.90 # Las tuplas son inmutables, constantes, las listas no

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Luka"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print((type(my_tuple)))

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple # 'del' elinima cualquier tipo de variable
#print(my_tuple) NameError: name 'my_tuple' is not defined