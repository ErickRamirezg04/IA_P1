#Excepciones: Como evitar errores triviales en el codigo

#Cuando los datos no son los que deberian ser
#type(value) is int

#Pedir perdon cuando ocurren los errores en vez de evitarlos
#try:
	# Es un lugar donde
	# tu puedes hacer algo 
    # sin pedir permiso.
#except:
	# Es un espacio dedicado  
    # exclusivamente para pedir perdón.

try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)        
except:
    print('No se que hacer con', value)

#Hacerlo dependiendo del error
try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)        
except ValueError:
    print('No se que hacer con', value)    
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.')

#La opcion predeterminada
try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)        
except ValueError:
    ('No se que hacer con.')    
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.')    
except:
    print('Ha sucedido algo extraño, ¡lo siento!')

#Excepciones utiles:
#ZeroDivisionError: Cuando quieres uan division con cero
#ValueError: Valor inaceptable
#TypeError: Intentas aplicar un dato cuyo tipo no se pueden en ese contexto
#AttributeError: Intentas aplicar un metodo que no existe para ese elemento
#SyntaxError: Aplicación erronea de la gramatica de python