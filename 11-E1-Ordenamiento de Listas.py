#Ordenamiento de listas
#Ordenamiento burbuja, la idea es llevar el numero mas alto hasta la posicion deseada
#Y repetir el proceso las veces que sea necesario para ordenas la lista
my_list = [8, 10, 6, 2, 4]  # lista a ordenar
swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.
 
while swapped:
    swapped = False  # no hay intercambios hasta ahora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # ¡ocurrió el intercambio!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
 
print(my_list)

#Mediante Comando
#Sort: de menor a mayor
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

#Reverse: Invierte
lst = [5, 3, 1, 2, 4]
print(lst)
 
lst.reverse()
print(lst)  # output: [4, 2, 1, 3, 5]

#Tambien sirve con caracteres
lst = ["D", "F", "A", "Z"]
lst.sort()
 
print(lst)