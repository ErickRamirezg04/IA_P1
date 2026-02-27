#Aplicaciones Avanzadas de listas
#Comprension de listas: se usa para llenar listas masivas de golpe
squares = [x ** 2 for x in range(10)]

#Arreglos de dos dimensiones o matrices: Lista de listas
board = []
 
for i in range(8):
    row = ["EMPTY" for i in range(8)]
    board.append(row)

#De forma corta
    board = [["EMPTY" for i in range(8)] for j in range(8)]

#Acceso a los elementos: El acceso al campo seleccionado del tablero
#requiere dos índices - el primero selecciona la fila; el segundo -
#el número del campo dentro de la fila, el cual es un número de columna.
board[4][2] = "KNIGHT"

#Empezamos de lo particular a lo general
#Control de habitaciones
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
rooms[1][9][13] = True