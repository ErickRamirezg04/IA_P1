# LAB: PALÍNDROMO
# -----------------------------------------------------------------------------
def verificar_palindromo(texto_usuario):
    # Eliminar espacios y convertir a mayúsculas para comparar 
    texto_limpio = texto_usuario.replace(' ', '').upper()
    
    # Un palíndromo debe tener más de un carácter y leerse igual al revés 
    if len(texto_limpio) > 1 and texto_limpio == texto_limpio[::-1]:
        return "Es un palíndromo"
    else:
        return "No es un palíndromo"