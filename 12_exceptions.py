### Exceptions Handling ###

number_one = 5
number_two = 1
number_two = "1"

# try except

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except: 
    # Se ejecuta si se produce una excepción
    print("Se ha producido un error")

# try axcept else
    
try:
    print(number_one + number_two)
    print("No se ha producido un error")
except: 
    print("No se cumplió")
else:
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
    
# try axcept else finally
    
try:
    print(number_one + number_two)
    print("No se ha producido un error")
except: 
    print("No se cumplió")
else: # Opcional
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally: # Opcional
    # Se ejecuta siempre
    print("La ejecución continúa")
    
# exceptions por tipo

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except ValueError: 
    # Se ejecuta si se produce una excepción
    print("Se ha producido un ValueError")
except TypeError: 
    # Se ejecuta si se produce una excepción
    print("Se ha producido un TypeError")
    
# Captura de la información de la excepción

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except TypeError as error: 
    print(error)
except Exception as error:
    print(error)
    
