#Funciones parametrizadas
#Los parametros se definen dentro de la funcion y solo reciben datos cuando se
#llaman
def message(number):
    print("Ingresa un número:", number)
message(1)

def mensaje(what, number):
    print("Ingresa", what, "número", number)
 
mensaje("teléfono", 11)
mensaje("precio", 5)
mensaje("número", "number")

#Paso de parametros posicionales, el orden se decide desde la funcion
def my_function(a, b, c):
    print(a, b, c)
 
my_function(1, 2, 3)

#paso de argumentos por palabra clave
def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)
 
introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")

#Combinacion de ambos: Tener cuidado de no asignar mas de un valor a un solo
#argumento
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
adding(3, c = 1, b = 2)

#Puedes asignar valores desde la funcion y usarlos o no
def introduccion(first_name="Juan", last_name="González"):
    print("Hola, mi nombre es", first_name, last_name)
introduccion(last_name="Rodríguez")