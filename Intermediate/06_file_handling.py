### File Handling ###

import os

# .txt file

txt_file = open("Intermediate/my_file.txt", "w+",encoding='utf-8') # r para leer y w para escribir. r+ Leer y escribir

txt_file.write("Mi nombre es Luis\nMi apeliido es Gordon\n22 años\nY mi lenguaje preferido es python")
txt_file.close()

txt_file = open("Intermediate/my_file.txt", "r+",encoding='utf-8')
#print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readline())
#print(txt_file.readline())
#print(txt_file.readlines())
for line in txt_file.readlines():
    print(line)
    
txt_file.write("\nAunque también me gusta PHP")
print(txt_file.readline())

txt_file.close()

#os.remove("Intermediate/my_file.txt")


# .json file

import json

json_file = open("Intermediate/my_file.json", "w+")
json_test = {
    "name":"Brais",
    "surname":"Gordon", 
    "age":22, 
    "language":"Python",
    "website":"https://lgordon.online"
    }

json.dump(json_test, json_file, indent = 2) # El número en indent hace referencia a los espacios de separación

json_file.close()

with open("Intermediate/my_file.json") as my_other_json:
    for line in my_other_json.readlines():
        print(line)
        
json_dict = json.load(open("Intermediate/my_file.json")) # Leer el fichero
print(json_dict)
print(type(json_dict)) # Devuelve un diccionario

# .csv file

import csv

csv_file = open("Intermediate/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Luis", "Gordon", 22, "Python", "https://lgordon.online"])
csv_file.close()

with open("Intermediate/my_file.csv") as my_other_csv:
    for line in my_other_csv:
        print(line)

# .xlsx file

#import xlrd # Debe instalarse el módulo

# .xml file

import xml