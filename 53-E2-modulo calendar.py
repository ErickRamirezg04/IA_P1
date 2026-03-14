# MÓDULO CALENDAR
# -----------------------------------------------------------------------------
# Permite generar calendarios y obtener información sobre días y meses

import calendar

# --- Funciones Básicas ---
# calendar(año): Devuelve un calendario multilínea para todo el año[cite: 4].
print(calendar.calendar(2023))

# month(año, mes): Devuelve el calendario de un mes específico[cite: 4].
print(calendar.month(2023, 12))

# setfirstweekday(): Cambia el primer día de la semana (0=Lunes, 6=Domingo)[cite: 4].
calendar.setfirstweekday(calendar.SUNDAY)

# weekday(año, mes, día): Devuelve el día de la semana para una fecha dada[cite: 4].
dia_indice = calendar.weekday(2023, 12, 24) # Devuelve el número del día [cite: 4]

# --- Clase Calendar e Iteradores ---
obj_cal = calendar.Calendar()

# itermonthdays(año, mes): Itera sobre los números de los días del mes[cite: 4].
# Los días fuera del mes en la primera/última semana se representan como 0[cite: 4].
for dia_it in obj_cal.itermonthdays(2023, 12):
    print(dia_it, end=" ")