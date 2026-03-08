#Operaciones con Cadenas

#min(): Esta función encuentra el elemento mínimo de la secuencia pasada como
#argumento.
# Demonstración de min() - Ejemplo 1:
print(min("aAbByYzZ"))


# Demonstración de min() - Ejemplos 2 y 3:
t = 'Los Caballeros Que Dicen "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))

#max(): encuentra el elemento máximo de la secuencia.
# Demostración de max() - Ejemplo 1:
print(max("aAbByYzZ"))


# Demostración de max() - Ejemplo 2 y 3:
t = 'Los Caballeros Que Dicen "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))

#El método index() (es un método, no una función) busca la secuencia desde el
#principio, para encontrar el primer elemento del valor especificado en su argumento.
# Demonstración del método index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

#La función list() toma su argumento (una cadena) y crea una nueva lista que contiene
#todos los caracteres de la cadena, uno por elemento de la lista.
# Demostración de la función list():
print(list("abcabc"))

#El método count() cuenta todas las apariciones del elemento dentro de la
#secuencia. La ausencia de tal elemento no causa ningún problema.
# Demostración del método count():
print("abcabc".count("b"))
print('abcabc'.count("d"))