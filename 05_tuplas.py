### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (22, 1.87, "Luis", "Gordon", "Luis")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Luis")) # Cuenta el cuantas veces está el elemento
print(my_tuple.index("Luis")) # Devuelve el indice del elemento
print(my_tuple.index("Gordon"))

my_tuple[1] = 1.90 # Las tuplas son inmutables, constantes, las listas no
print(my_tuple)
