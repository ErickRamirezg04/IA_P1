# LAB: EVALUANDO RESULTADOS (GESTIÓN DE EXCEPCIONES PERSONALIZADAS)
# -----------------------------------------------------------------------------
from os import strerror

class ErrorDatosEstudiante(Exception):
    """Excepción base para errores en el archivo de estudiantes."""
    pass

class LineaCorrupta(ErrorDatosEstudiante):
    def __init__(self, num_linea, contenido):
        super().__init__(f"Error en línea {num_linea}: {contenido}")

class ArchivoVacio(ErrorDatosEstudiante):
    def __init__(self):
        super().__init__("El archivo seleccionado no contiene datos.")

def procesar_calificaciones(ruta_archivo):
    registro_puntos = {}
    try:
        with open(ruta_archivo, "rt") as f_datos:
            lineas_est = f_datos.readlines()
            
        if not lineas_est:
            raise ArchivoVacio()

        for indice, contenido_linea in enumerate(lineas_est):
            partes = contenido_linea.split()
            # Se esperan 3 columnas: Nombre, Apellido, Puntos 
            if len(partes) != 3:
                raise LineaCorrupta(indice + 1, contenido_linea)
            
            id_estudiante = f"{partes[0]} {partes[1]}"
            try:
                valor_puntos = float(partes[2])
            except ValueError:
                raise LineaCorrupta(indice + 1, contenido_linea)
            
            # Acumular puntos en el diccionario 
            registro_puntos[id_estudiante] = registro_puntos.get(id_estudiante, 0) + valor_puntos

        # Imprimir resultados ordenados alfabéticamente 
        for est in sorted(registro_puntos.keys()):
            print(f"{est}\t{registro_puntos[est]}")

    except IOError as e:
        print(f"Error de sistema: {strerror(e.errno)}")