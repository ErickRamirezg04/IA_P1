# LAB 2: Simulador de Display LED (7 Segmentos)
# -----------------------------------------------------------------------------
# Representación de dígitos del 0 al 9 en formato binario de 7 segmentos
patrones_led = ['1111110', '0110000', '1101101', '1111001', '0110011', 
                '1011011', '1011111', '1110000', '1111111', '1111011']

def mostrar_numero_led(valor_numerico):
    cadena_digitos = str(valor_numerico)
    # Creamos 5 líneas vacías para representar la altura del display
    filas_display = ["" for _ in range(5)]
    
    for digito in cadena_digitos:
        # Estructura 3x5 para cada dígito
        celdas = [[' ' for _ in range(3)] for _ in range(5)]
        patron = patrones_led[ord(digito) - ord('0')]
        
        # Lógica de mapeo de segmentos a caracteres '#'
        if patron[0] == '1': celdas[0][0] = celdas[0][1] = celdas[0][2] = '#'
        if patron[1] == '1': celdas[0][2] = celdas[1][2] = celdas[2][2] = '#'
        if patron[2] == '1': celdas[2][2] = celdas[3][2] = celdas[4][2] = '#'
        if patron[3] == '1': celdas[4][0] = celdas[4][1] = celdas[4][2] = '#'
        if patron[4] == '1': celdas[2][0] = celdas[3][0] = celdas[4][0] = '#'
        if patron[5] == '1': celdas[0][0] = celdas[1][0] = celdas[2][0] = '#'
        if patron[6] == '1': celdas[2][0] = celdas[2][1] = celdas[2][2] = '#'
        
        for i in range(5):
            filas_display[i] += "".join(celdas[i]) + " "

    for fila in filas_display:
        print(fila)