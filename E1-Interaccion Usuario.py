#Input: Guarda datos registrados por el usuario desde la consola
#Lo convierte en una cadena, no sirve para operaciones
anything = input("Dime lo que sea...")
print("Hmm...", anything, "...¿en serio?")

#En caso de ser necesario para operaciones se debe asignar tipo de dato
anything = float(input("Ingresa un número: "))
something = anything ** 2.0
print(anything, "a la potencia de 2 es", something)

#Se pueden concatenar cadenas
fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + fnam + " " + lnam + ".")

#Replicación se usa el asterisco en una cadena y un numero para repetir
#string * number
#number * string