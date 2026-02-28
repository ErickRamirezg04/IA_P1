#Tuplas y Diccionarios
#una secuencia es un tipo de dato que puede ser escaneado por el bucle for.
#Los datos mutables pueden ser actualizados libremente en cualquier momento
#Una tupla es una secuencia inmutable. Se puede comportar como una lista
#pero no puede ser modificada en el momento.

#Tuplas: Es una lista, pero, donde no puedes modificar nada de ella
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125
print(tuple_1)
print(tuple_2)

#De un solo elemento
one_element_tuple_1 = (1, )
one_element_tuple_2 = 1.,

#Lectura: Igual a las listas
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)

#Acciones basicas
    my_tuple1 = (1, 10, 100)

t1 = my_tuple1 + (1000, 10000)
t2 = my_tuple1 * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple1)
print(-10 not in my_tuple1)

var = 123

t3 = (1, )
t4 = (2, )
t5 = (3, var)

t3, t4, t5 = t4, t5, t3

print(t3, t4, t5)

#Se pueden desempaquetar las tuplas
tup = 1, 2, 3
a, b, c = tup

print(a * b * c)

#Encontrar duplicados
tup6 = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup6.count(2)

print(duplicates)

#Convertir listas a tuplas
my_list = ["car", "Ford", "flower", "Tulip"]

t = tuple(my_list)
print(t)

#Convertir tupla a diccionario
colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors)
print(colors_dictionary)

#Diccionario
#la palabra que se esta buscando se denomina key. La palabra que se obtiene del
#diccionario es denominada value.
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}
dictionary = {"cat": "gato", "perro": "chien", "caballo": "cheval"}
words = ['gato', 'león', 'caballo']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario")


print(dictionary)
print(phone_numbers)
print(empty_dictionary)
#print(dictionary['gato'])
print(phone_numbers['Suzy'])

#Metodo Keys
#dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])

#Items
#dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

for spanish, french in dictionary.items():
    print(spanish, "->", french)

#Reemplazo
dictionary['gato'] = 'minou'
#Sorted para ordenar
#for key in sorted(dictionary.keys()):

#Agregar nuevas claves
#dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

dictionary['cisne'] = 'cygne'
print(dictionary)

dictionary.update({"pato": "canard"})
print(dictionary)

#Eliminar clave
del dictionary['perro']
print(dictionary)

#Eliminar ultimo elemento
dictionary.popitem()
print(dictionary)

#Unir diccionarios
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)

#Uso de For
colors = {
    "blanco": (255, 255, 255),
    "gris": (128, 128, 128),
    "rojo": (255, 0, 0),
    "verde": (0, 128, 0)
    }

for col, rgb in colors.items():
    print(col, ":", rgb)


#Trabajo en conjunto
school_class = {}

while True:
    name = input("Ingresa el nombre del estudiante: ")
    if name == '':
        break
    
    score = int(input("Ingresa la calificación del estudiante (0-10): "))
    if score not in range(0, 11):
	    break
    
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)