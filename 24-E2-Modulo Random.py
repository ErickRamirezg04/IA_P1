#Modulo Random
#Funcion random del modulo: random() (no debe confundirse con el nombre del
#módulo) produce un número flotante x entre el rango (0.0, 1.0) -
#en otras palabras: (0.0 <= x < 1.0).
from random import random

for i in range(5):
    print(random())

#Funcion seed: es capaz de directamente establecer la semilla del generador
#Inicialización con valor entero: Siempre igual
from random import random, seed

seed(0)

for i in range(5):
    print(random())

#Seed sencilla: establece la semilla con la hora actual.
seed()

#Para valores enteros
from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))
#Desventaja: Puede producir valores repetidos
from random import randint

for i in range(10):
    print(randint(1, 10), end=',')

#Funcion choice: Elige un dato aleatorio de la secuencia de entrada
#Funcion sample: Crea una muestra de cierto tamaño de los elementos de la secuencia
from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))