# LAB 3: Validador de Sudoku
# -----------------------------------------------------------------------------
def validar_set_sudoku(grupo_nueve):
    # Verifica que el grupo contenga exactamente los números del 1 al 9
    return sorted(list(grupo_nueve)) == [chr(x + ord('0')) for x in range(1, 10)]

def procesar_sudoku():
    matriz_sudoku = []
    # Captura de 9 filas
    for i in range(9):
        fila_entrada = input(f"Ingresa fila #{i+1}: ")
        if len(fila_entrada) == 9 and fila_entrada.isdigit():
            matriz_sudoku.append(fila_entrada)
        else:
            print("Error: Se requieren 9 dígitos.")
            return

    es_valido = True
    # Validación de filas y columnas simultáneamente
    for i in range(9):
        if not validar_set_sudoku(matriz_sudoku[i]): # Filas
            es_valido = False
        columna_temp = [matriz_sudoku[j][i] for j in range(9)] # Columnas
        if not validar_set_sudoku(columna_temp):
            es_valido = False

    # Validación de subcuadrados 3x3
    for f in range(0, 9, 3):
        for c in range(0, 9, 3):
            cuadro = ""
            for i in range(3):
                cuadro += matriz_sudoku[f+i][c:c+3]
            if not validar_set_sudoku(list(cuadro)):
                es_valido = False
    
    print("Sudoku Válido: ", "Si" if es_valido else "No")