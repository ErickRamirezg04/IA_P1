# LAB 4: El Dígito de la Vida (Reducción Numerológica)
# -----------------------------------------------------------------------------
def calcular_digito_vida(fecha_str):
    # El algoritmo suma los dígitos hasta que solo quede uno
    while len(fecha_str) > 1:
        suma_digitos = sum(int(d) for d in fecha_str)
        fecha_str = str(suma_digitos)
    return fecha_str

# Ejemplo de uso:
# print(calcular_digito_vida("19991229"))