#MÉTODOS DE CADENAS 2
# -----------------------------------------------------------------------------

# lower(): Crea una copia de la cadena convirtiendo todo a minúsculas.
print("SiGmA=60".lower()) 

# lstrip(caracteres): Elimina espacios iniciales o caracteres específicos por la izquierda.
print("[" + " tau ".lstrip() + "]") 
print("www.cisco.com".lstrip("w.")) 

# replace(antiguo, nuevo, cantidad): Reemplaza apariciones de una subcadena por otra.
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", "")) 
print("This is it!".replace("is", "are", 1)) # Reemplaza solo la primera aparición [cite: 67]
print("This is it!".replace("is", "are", 2))

# rfind(subcadena): Similar a find, pero inicia la búsqueda desde el final (derecha).
print("tau tau tau".rfind("ta")) 
print("tau tau tau".rfind("ta", 9)) 
print("tau tau tau".rfind("ta", 3, 9)) 

# rstrip(caracteres): Elimina espacios finales o caracteres específicos por la derecha.
print("[" + " upsilon ".rstrip() + "]") 
print("cisco.com".rstrip(".com")) 

# split(): Divide una cadena en una lista de subcadenas basándose en espacios en blanco.
print("phi\nchi\npsi".split()) 

# startswith(subcadena): Comprueba si la cadena inicia con el argumento especificado.
print("omega".startswith("meg")) 
print("omega".startswith("om")) 

# strip(): Combina lstrip y rstrip para limpiar ambos extremos de la cadena.
print("[" + " aleph ".strip() + "]")

# swapcase(): Intercambia mayúsculas por minúsculas y viceversa.
print("Yo solo sé que no sé nada".swapcase()) 

# title(): Convierte la primera letra de cada palabra a mayúscula.
print("Yo solo sé que no sé nada. Parte 1.".title()) 

# upper(): Crea una copia de la cadena convirtiendo todo a mayúsculas.
print("Yo solo sé que no sé nada. Parte 2.".upper()) 