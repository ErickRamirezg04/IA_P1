#Importar entidades especificas del modulo(No puedes usar las que no llamaste)
#from math import pi

#Se puede redefinir el significado de las entidades una vez llegan al namespace
#Recodar que las entidades del modulo solo tienen alcance despues de que se
#mandan a llamar
from math import sin, pi

print(sin(pi / 2))

pi = 3.14


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


print(sin(pi / 2))

#Importar todas las entidades del modulo
#from module import *

#Clave as para renombrar el modulo
#import module as alias

import math as m
    
print(m.sin(m.pi/2))

#Renombrar entidades del modulo
#from module import name as alias

#Renombrar varias entidades
#from module import n as a, m as b, o as c