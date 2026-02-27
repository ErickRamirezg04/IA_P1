#Bucles
#While repite el bucle hasta que ya no haya nada que hacer
counter = 5
while counter != 0:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)

#for explora colleciones de datos elemento por elemento
#primer num inicio
#segundo num primer valorq que no tomara
#tercer num incremento
for i in range(2, 8, 3):
    print("El valor de i es", i)

#break: termina por completo el ciclo y desarrolla la siguiente instruccion
#continue: llega al final del for e inicia la siguiente iteración
#Tambien puede usar else
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

for i in range(5):
    print(i)
else:
    print("else:", i)

#LABORATORIO: Prueba pisos de piramide
blocks = int(input("Ingresa el número de bloques: "))
pisos = 0

for i in range(1,blocks+1):
    
    blocks-=i
    if blocks<i:
        pisos=i
        break
print("La altura de la pirámide:", pisos)