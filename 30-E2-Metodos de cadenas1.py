#MÉTODOS DE CADENAS 1
# -----------------------------------------------------------------------------

# capitalize(): Convierte el primer carácter en mayúscula y el resto en minúsculas.
print("Alpha".capitalize()) 
print('ALPHA'.capitalize()) 
print(' Alpha'.capitalize()) # Nota: Si hay un espacio al inicio, no capitaliza la letra [cite: 5]
print('123'.capitalize()) 
print("αβγδ".capitalize()) 

# center(ancho, caracter_relleno): Centra la cadena en un espacio definido.
# Si el ancho es menor a la longitud de la cadena, devuelve la cadena original.
print('[' + 'Beta'.center(2) + ']') 
print('[' + 'Beta'.center(4) + ']') 
print('[' + 'Beta'.center(6) + ']') 
print('[' + 'gamma'.center(20, '*') + ']')

# endswith(subcadena): Devuelve True si la cadena termina con el argumento especificado.
if "epsilon".endswith("on"): 
    print("si") 
else:
    print("no") 

# find(subcadena, inicio, fin): Busca la subcadena y devuelve el índice de la 
# primera aparición. Devuelve -1 si no la encuentra.
print("Eta".find("ta")) 
print("Eta".find("mma")) 
print('kappa'.find('a', 2)) # Empieza a buscar desde el índice 2 [cite: 23]
print('kappa'.find('a', 1, 4)) # Busca entre los índices 1 y 3 [cite: 25]

# isalnum(): Verifica si todos los caracteres son alfanuméricos (letras o números).
print('lambda30'.isalnum()) 
print('lambda'.isalnum()) 
print('30'.isalnum()) 
print('@'.isalnum()) # False, contiene caracteres especiales [cite: 31]
print('lambda_30'.isalnum()) # False, el guion bajo no es alfanumérico [cite: 32]

# isalpha(): Verifica si la cadena contiene únicamente letras.
print("Moooo".isalpha()) 
print('Mu40'.isalpha()) 

# isdigit(): Verifica si la cadena contiene únicamente dígitos numéricos.
print('2018'.isdigit()) 
print("Year2019".isdigit()) 

# islower(): Verifica si todos los caracteres alfabéticos están en minúsculas.
print("Moooo".islower()) 
print('moooo'.islower()) 

# isspace(): Verifica si la cadena contiene únicamente espacios en blanco (incluye saltos de línea).
print('\n '.isspace()) 
print(" ".isspace()) 
print("mooo mooo mooo".isspace()) 

# isupper(): Verifica si todos los caracteres alfabéticos están en mayúsculas.
print("Moooo".isupper()) 
print('moooo'.isupper()) 
print('MOOOO'.isupper()) 

# join(iterable): Une los elementos de una lista/iterable usando la cadena base como separador.
# Todos los elementos deben ser de tipo string.
print(",".join(["omicron", "pi", "rho"])) 