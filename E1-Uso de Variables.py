#Variable: Almacenaiento de valores o datos para su uso en el codigo
#No es necesario asignar tipo
#Empezar con letra minuscula y separar con guiones bajos, no usar reservadas
#Distingue mayusculas y minusculas
var = 1
print(var)
#Puede combinar texto con variables
var = "3.8.5"
print("Python version: " + var)
#Para aplicar operaciones al valor actual

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")
#round limita el numero de decimales

a = 6
b = 3
a /= 2 * b
print(a)