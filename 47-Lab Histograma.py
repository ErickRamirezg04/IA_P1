# LAB 7: Gestión de Archivos e Histograma de Frecuencia
# -----------------------------------------------------------------------------
from os import strerror

def generar_histograma_letras(nombre_archivo):
    conteo_letras = {}
    try:
        # Modo 'rt': lectura de texto
        with open(nombre_archivo, "rt") as f_lectura:
            for linea in f_lectura:
                for char in linea:
                    if char.isalpha():
                        c = char.lower()
                        conteo_letras[c] = conteo_letras.get(c, 0) + 1
        
        # Ordenar por frecuencia descendente usando una función lambda
        ordenado = sorted(conteo_letras.items(), key=lambda x: x[1], reverse=True)
        
        # Escritura de resultados en un nuevo archivo .hist
        with open(nombre_archivo + ".hist", "wt") as f_salida:
            for letra, freq in ordenado:
                f_salida.write(f"{letra} -> {freq}\n")
                
    except IOError as error_archivo:
        print("Error al procesar archivo:", strerror(error_archivo.errno))