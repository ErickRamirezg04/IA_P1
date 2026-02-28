#Instruccion return sin expresion
def happy_new_year(wishes = True):
    print("Tres...")
    print("Dos...")
    print("Uno...")
    if not wishes:
        return

    print("¡Feliz año nuevo!")

#return con expresion
def boring_function():
    return 123

x = boring_function()

print("La función boring_function ha devuelto su resultado. Es:", x)

#None: No olvides esto: si una función no devuelve un cierto valor
#utilizando una cláusula de expresión return,se asume que devuelve implícitamente None.
def strange_function(n):
    if(n % 2 == 0):
        return True
print(strange_function(2))
print(strange_function(1))

#Se pueden enviar listas como argumento de funciones
def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s

print(list_sum([5, 4, 3]))

#Se puede regresar listas con el return
def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))