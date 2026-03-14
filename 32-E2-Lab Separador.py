# LAB 1: Tu propio separador
# -----------------------------------------------------------------------------
def mi_propio_split(cadena_entrada):
    # Devuelve una lista vacía si la cadena no tiene contenido útil
    if cadena_entrada == "" or cadena_entrada.isspace():
        return []
    
    lista_resultado = []
    palabra_temporal = ""
    # Flag para saber si estamos procesando caracteres de una palabra
    dentro_de_palabra = not cadena_entrada[0].isspace()

    for caracter in cadena_entrada:
        if dentro_de_palabra:
            if not caracter.isspace():
                palabra_temporal += caracter
            else:
                # Al encontrar un espacio, guardamos la palabra acumulada
                lista_resultado.append(palabra_temporal)
                dentro_de_palabra = False
        else:
            if not caracter.isspace():
                dentro_de_palabra = True
                palabra_temporal = caracter
    
    # Agregar la última palabra si el ciclo terminó sin un espacio final
    if dentro_de_palabra:
        lista_resultado.append(palabra_temporal)
    return lista_resultado

# Pruebas del separador
print(mi_propio_split("Ser o no ser, esa es la cuestión"))
print(mi_propio_split(" abc "))