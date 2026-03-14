# LAB: MÓDULO OS - BUSCADOR RECURSIVO DE DIRECTORIOS
# -----------------------------------------------------------------------------
import os

class BuscadorDirectorios:
    def buscar_en_ruta(self, ruta_actual, objetivo):
        try:
            # Cambiar al directorio para explorar 
            os.chdir(ruta_actual)
        except OSError:
            return

        directorio_base = os.getcwd()
        for elemento in os.listdir("."):
            # Si el elemento es el que buscamos, imprimimos la ruta completa 
            if elemento == objetivo:
                print(f"Encontrado: {directorio_base}/{elemento}")
            
            # Si es una carpeta, entramos recursivamente 
            if os.path.isdir(elemento):
                nueva_ruta = f"{directorio_base}/{elemento}"
                self.buscar_en_ruta(nueva_ruta, objetivo)
                # Volver al directorio padre tras la recursión
                os.chdir("..")

# Uso: buscador = BuscadorDirectorios()
# buscador.buscar_en_ruta("./tree", "python")