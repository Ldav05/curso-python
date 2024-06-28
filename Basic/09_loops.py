### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi condición es mayor o igual ")
    
print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detienen la ejecución")
        break # Detener la ejecución
    print(my_condition)
    
print("La ejecució continúa")

# For 

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list: # Esta sintaxis es parecida a la de un Foreach 
    print(element)
    
my_tuple = (22, 1.88, "Luis", "Gordon", "Luis")

for element in my_tuple:
    print(element)

my_set = {"Luis", "Gordon", 22}

for element in my_set:
    print(element)

my_dict = {
    "Nombre": "Luis",
    "Apellido": "Gordon",
    "Edad": 22
}

for element in my_dict.values(): # Como llamamos la función values() nos imprime los valores
    print(element)
    
for element in my_dict:
    print(element)
    if element == "Edad":
        break
    print("Se ejecuta")
else:
    print("El bucle for para dicci onario ha finalizado")
    
print("La ejecución continúa")

for element in my_dict.values(): # Como llamamos la función values() nos imprime los valores
    print(element)
    
for element in my_dict:
    print(element)
    if element == "Edad":
        continue # Continúa deteniento la ejecución desde ese punto, regresando al bucle
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")
    