#Funciones y alcances
#una variable que existe fuera de una función tiene alcance
#dentro del cuerpo de la función.
#el alcance de una variable existente fuera de una función solo se puede
#implementar dentro de una función cuando su valor es leído.
#El asignar un valor hace que la función cree su propia variable.

#Palabra clave global: Orden al programa para abstenerse de crear una nueva
#variable dentro de la funcion, se empleará la del exterior
global name1, name2

#La varibale solo actua dentro de la funcion: ERROR
def message():
    alt = 1
    print("¡Hola, mundo!")
 
print("alt")

#El print de debajo toma el valor fuera de la funcion
a = 1
 
def fun():
    a = 2
    print(a)
 
fun()
print(a)

#El valor global afecta solo hasta los limites de donde la funcion fue llamada
b = 1

def fun():
    global b
    b = 2
    print(b)

fun()
b = 3
print(b)

#El print de debajo toma el valor de la variable global porque llama a la
#funcion justamente antes, se ignora el 3
c = 1

def fun():
    global c
    c = 2
    print(c)

c = 3
fun()
print(c)