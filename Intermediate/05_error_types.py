### Error types ###

# SyntaxError
# print "¡Hola comunidad!" # Descomentar para Error
print("¡Hola comunidad!")

# NameError
language = "Spanish" # Comentar para Error
print(language)

# IndexError
My_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(My_list[0])
print(My_list[4])
print(My_list[-1])
#print(My_list[5]) # Descomentar para Error

# ModuleNotFoundError
#import maths # Descomentar para Error
import math 

# AttributeError
#print(math.PI) # Descomentar para Error
print(math.pi)

# KeyError
my_dict = {"Nombre":"Brais", "Apellido":"Gordon", "Edad":22, 1:"Python"}
print(my_dict["Edad"])
#print(my_dict["Apelido"]) # Descomentar para Error
print(my_dict["Apellido"])

# TypeError
#print(My_list["0"]) # Descomentar para Error
print(My_list[0])

# ImportError
#from math import PI # Descomentar para Error
from math import pi
print(pi)

# ValueError
#my_int = int("10")
my_int = int("10 Años")
print(type(my_int))

# ZeroDivisionError
Print(4/2)
#print(4/0) # Descomentar para Error