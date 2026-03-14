# MÓDULO OS (SISTEMA OPERATIVO)
# -----------------------------------------------------------------------------
import os

# os.name: Nombre del sistema operativo (posix, nt, etc.).
print(os.name) 

# Creación y eliminación de directorios.
try:
    os.mkdir("test_dir") # Crea un directorio [cite: 357]
    print(os.listdir()) # Lista contenidos [cite: 357]
    print(os.getcwd())  # Directorio actual de trabajo [cite: 357]
    os.rmdir("test_dir") # Elimina el directorio [cite: 358]
except FileExistsError:
    print("El directorio ya existe.")

