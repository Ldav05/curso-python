### Regular Expressions ###

import re

my_string = "Esta es la lección número 7: Expresiones Regulares"
my_other_string = "Esta no es la lecci+on número 6: Manejo de ficheros"

print(re.match("Esta es la lección", my_string, re.I))
print(re.match("Esta es la lección", my_other_string))


### revisar repositorio de MoureDev