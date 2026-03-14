# LAB DATETIME

# -----------------------------------------------------------------------------
from datetime import datetime


instante_lab = datetime(2020, 11, 4, 14, 53, 0) # Fecha del lab [cite: 3, 5]

# Renombrado de variables para evitar interferencias
fmt_iso = instante_lab.strftime("%Y/%m/%d %H:%M:%S")
fmt_completo = instante_lab.strftime("%y/%B/%d %H:%M:%S %p")
fmt_abreviado = instante_lab.strftime("%a, %Y %b %d")
fmt_dia_semana = instante_lab.strftime("Día de la semana: %u") # %u para número de día [cite: 3, 5]
fmt_dia_año = instante_lab.strftime("Día del año: %j")
fmt_num_semana = instante_lab.strftime("Número de semana en el año: %W")

print(fmt_iso)
print(fmt_completo)
print(fmt_abreviado)
print(fmt_dia_semana)
print(fmt_dia_año)
print(fmt_num_semana)