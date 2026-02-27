#Funciones basicas de Listas 
#Lista: Variable que almacena mas de un elemento, no debe ser del mismo tipo
#Puede anidarse con otras listas
#Siempre empiezan desde cero
numbers = [10, 5, 7, 2, 1]

numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  # Imprimiendo el contenido de la lista original.

numbers[0] = 111
print("\nContenido de la lista con cambio:", numbers)  # Imprimiendo contenido de la lista con 111.

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Contenido de la lista con intercambio:", numbers)  # Imprimiendo contenido de la lista con intercambio.

print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.

del numbers[1]  # Eliminando el segundo elemento de la lista.

#se pueden indices negativos pero varia con el numero de elementos
print(numbers[-2])

#agregar elementos a listas existentes
#list.append(value): coloca al final
#list.insert(location, value): coloca donde sea necesario y recorre la lista

my_list = []  # Creando una lista vacía.
#Asignar valores de la lista a una variable
my_list = [10, 1, 8, 3, 5]
total = 0
 
for i in my_list:
    total += i
 
print(total)

#Intercambio
variable_1 = 1
variable_2 = 2
 
variable_1, variable_2 = variable_2, variable_1

#Intercambio de elementos en toda la lista desde extremos
#for i in range(length // 2):
#    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
 
#print(my_list)
