### Sets ###

my_set = set()  # Definir un set
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Luis", "Gordon", 22}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Luka")

print(my_other_set) # Un set no es una estructura ordenada y no podemos acceder por medio de índices

my_other_set.add("Luka") # Un set no admite repetidos

print(my_other_set)

# Realizar búsquedas

print("Luka" in my_other_set)
print("Luca" in my_other_set)

# Eliminar elementos

my_other_set.remove("Luka")
print(my_other_set)

my_other_set.clear()
print(my_other_set)
print(len(my_other_set))

del my_other_set # Elimina el set por completo, contenido e instancia
#print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {"Luis", "Gordon", 22}
my_list = list(my_set) # Es arriesgado porque el set cada vez que se ejecuta, cambia de orden
print(my_list)
print(my_list[0])

my_other_set = {"Php", "Javascript", "Python"}

# Unir dos sets

my_new_set = my_set.union(my_other_set)
print(my_new_set)
print(my_new_set.union(my_new_set)) # Como no acepta repetidos, no cambia el contenido del set
print(my_new_set.union(my_new_set).union(my_set).union({"C#", "Java"}))

# Diferencias entre dos sets 

print(my_new_set.difference(my_set))