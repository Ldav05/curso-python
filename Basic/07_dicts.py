### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

# Podemos almacenar datos de tipo clave-valor

my_other_dict = {"Nombre":"Luis", "Apellido":"Gordon", "Edad":22, 1:"Python"}
print(my_other_dict)

my_dict = {
    "Nombre":"Luis", 
    "Apellido":"Gordon", 
    "Edad":22, 
    "Lenguajes": {"Python", "PHP", "Javascript" },
    1: 1.88
    }

print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

# Actualizar

my_dict["Nombre"] = "David"
print(my_dict["Nombre"])

print(my_dict[1])

# Agregar un nuevo campo al diccionario

my_dict["Calle"] = "Calle Luka"
print(my_dict)

# Eliminar

del my_dict["Calle"] # Como le pasamos un elemento en concreto, lo elimina, si no lo hicieramos, eliminaría todo el diccionario
print(my_dict)

# Verificar existencia de claves

print("Luis" in my_dict)
print("Apellido" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]
my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, )
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(my_new_dict.values()))
print(tuple(my_new_dict))
print(set(my_new_dict))