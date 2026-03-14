# TRABAJO CON ARCHIVOS (STREAMS)
# -----------------------------------------------------------------------------

from os import strerror

# Lectura de archivos de texto.
try:
    with open('text.txt', "rt") as file_stream: 
        char = file_stream.read(1) # Lee de carácter en carácter 
        while char != '':
            print(char, end='')
            char = file_stream.read(1)
except IOError as e:
    print("Error de E/S:", strerror(e.errno))

# Escritura en archivos binarios.
data_bytes = bytearray(10)
try:
    with open('file.bin', 'wb') as bin_file:
        bin_file.write(data_bytes)
except IOError as e:
    print("Error al escribir binario:", strerror(e.errno)) 