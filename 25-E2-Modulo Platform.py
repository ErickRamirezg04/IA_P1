#Modulo platform
#permite acceder a los datos de la plataforma subyacente, es decir, hardware,
#sistema operativo e información sobre la versión del intérprete.

#Funcion platform: Muestrs las capaz subyacentes
from platform import platform

platform(aliased = False, terse = False)
print(platform())
print(platform(1))
print(platform(0, 1))

#Funcion machine: Nombre generico del procesador que ejecuta el sistema operativo
from platform import machine

print(machine())

#Funcion processor: DEvuelve cadena con el nombre real del procesador
from platform import processor

print(processor())

#Funcion system: devuelve el nombre generico del sistema operativo
from platform import system

print(system())

#Funcion versio: Proporciona la version del sistema operativo
from platform import version

print(version())

#Funciones: python_implementation y python_version_tuple
from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)