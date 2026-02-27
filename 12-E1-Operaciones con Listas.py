#Operaciones con listas
#Copia de la direccion de la lista
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

#Rebanadas: Copia secciones especificas en una nueva lista
# : solos indican toda la lista
#my_list[inicio:fin] en realidas es desde 1 a (fin-1)
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

#del tambien sirve en conjunto con rebanadas
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

#operadores "in" y "not in"
#Comprueba si los elementos de la izquierda estan o no en la lista
#Devuelve true or false
#elem in my_list
#elem not in my_list

#Combinaciones con for
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
 
for i in my_list[1:]:
    if i > largest:
        largest = i
 
print(largest)