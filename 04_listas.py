### Lists ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [22, 24, 26, 28,30, 30, 34]

print(my_list)
print(len(my_list))

my_other_list = [22, 1.87, "Luis", "Gordon"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_other_list.count("Luis")) # Contar las veces que se repite un elemento dentro de la lista
#print(my_other_list[4]) IndexError
#print(my_other_list[-5]) IndexError

age, height, name, surname = my_other_list
print(name)

name, height,age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

print(my_list + my_other_list) # Concatenar dos listas
#print(my_list + my_other_list)

my_other_list.append("LukaDev") # Añade un nuevo elemento al final de la lista
print(my_other_list)

my_other_list.insert(1, "Red") # Inserta un elemento en la posición que se le indique
print(my_other_list)

my_other_list[1] = "Blue" # Reemplazar una posición en concreto
print(my_other_list)

my_other_list.remove("Blue") # Elimina elementos de la lista 
print(my_other_list)

my_list.remove(30)
print(my_list)

my_list.pop() # Elimina el último elemento de la lista
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2] # Elimina por indice
print(my_list)

my_new_list = my_list.copy() # Copiar una lista

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse() # Reordenar la lista al revés
print(my_new_list)

my_new_list.sort() # Ordenarlo dependiendo al criterio que se le asigne
print(my_new_list)

my_list.clear() # Elimina toda la lista
print(my_list)

print(my_new_list[1:2]) # Cortar, crear sublistas

my_list = "Hola Python"
print(my_list) 
print(type(my_list))