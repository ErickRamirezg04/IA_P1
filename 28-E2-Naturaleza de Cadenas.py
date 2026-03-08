#Naturaleza de las cadenas en Python

#La función len() empleada en las cadenas
#devuelve el número de caracteres que contiene el argumento. 
# Ejemplo 1
word = 'by'
print(len(word))
# Ejemplo 2
empty = ''
print(len(empty))
# Ejemplo 3
i_am = 'I\'m'
print(len(i_am))

#Cadenas multilinea
multiline = '''Línea #1
Línea #2'''

print(len(multiline))
#En total son 17 caracteres, El carácter que falta es simplemente invisible:
#es un espacio en blanco. Se encuentra entre las dos líneas de texto.

#Operaciones con cadenas
#En general, las cadenas pueden ser:
#Concatenadas o Replicadas.
#La primera operación la realiza el operador + (toma en cuenta que no es una
#adición o suma) mientras que la segunda por el operador *
#(toma en cuenta de nuevo que no es una multiplicación).
str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)

#Funcion ord(): Si deseas saber el valor del punto de código ASCII/UNICODE de
#un carácter específico
char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))

#chr(): Si conoces el punto de código (número) y deseas obtener el carácter
#correspondiente
print(chr(97))
print(chr(945))

# Indexando cadenas.

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()

# Iterando a través de una cadena.

the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

print()

# Rebanadas

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

#El operador in y not in no debería sorprenderte cuando se aplica a cadenas, simplemente
#comprueba si el argumento izquierdo (una cadena) se
#puede encontrar en cualquier lugar dentro del argumento derecho (otra cadena).
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)
print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)

#Añadir datos a la cadena
alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)