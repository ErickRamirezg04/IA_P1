#Funciones: Partes aisladas de codigo que realizan funciones especificas
#Permiten reducir el contenido de manera que no tengamos que copiar
#partes especificas

#Definicion basica
#def function_name():
#    cuerpo de la función

#Ejemplo de funcion
def message():
    print("Ingresar valor: ")
 
print("Inicia aqui.")
message()
print("Termina aqui.")
 
message()
a = int(input())

#Funcion con argumentos
def hello(name): # definiendo una función
    print("Hello,", name) # cuerpo de la función
 
 
name = input("Ingresa tu nombre: ")
 
hello(name) # invocación de la función