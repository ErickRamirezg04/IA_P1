# 4. MANEJO DE EXCEPCIONES
# -----------------------------------------------------------------------------

# Bloque try-except básico para captura de errores.
try:
    first_num = int(input("Ingresa el primer número: ")) 
    second_num = int(input("Ingresa el segundo numero: ")) 
    print(first_num / second_num) 
except:
    print("Esta operación no puede ser realizada.")

# Bloque try-except específico para diferentes errores.
try:
    x_val = int(input("Ingresa un número: ")) 
    y_val = 1 / x_val 
    print(y_val) 
except ZeroDivisionError:
    print("No puedes dividir entre cero, lo siento.")
except ValueError:
    print("Debes ingresar un valor entero..")
except Exception:
    print("Oh cielos, algo salió mal...") 

# assert: Verifica una condición; si es falsa, lanza AssertionError.
from math import tan, radians
try:
    angle_deg = int(input('Ingresa un angulo entero en grados: '))
    assert angle_deg % 180 != 90 # El ángulo no debe ser múltiplo impar de 90 [cite: 147]
    print(tan(radians(angle_deg))) 
except AssertionError:
    print("Error de aserción: Ángulo inválido para la tangente.")