# LAB: CONTADOR DE DÍAS ESPECÍFICOS EN EL AÑO
# Tarea: Crear una clase que cuente cuántas veces ocurre un día de la semana[cite: 4].
# -----------------------------------------------------------------------------
import calendar


class ContadorCalendario(calendar.Calendar):
    def contar_dias_semana_en_año(self, año_ref, dia_semana_ref):
        mes_actual = 1
        total_ocurrencias = 0
        
        while mes_actual <= 12:
            # monthdays2calendar devuelve semanas como tuplas (día_mes, día_semana) [cite: 4]
            for semana_lista in self.monthdays2calendar(año_ref, mes_actual):
                for dia_mes, dia_sem in semana_lista:
                    # Si el día de la semana coincide y no es un día de relleno (0) [cite: 4]
                    if dia_sem == dia_semana_ref and dia_mes != 0:
                        total_ocurrencias += 1
            mes_actual += 1
            
        return total_ocurrencias

# Renombrado de variables para la ejecución del Lab
manejador_cal = ContadorCalendario()
conteo_lunes = manejador_cal.contar_dias_semana_en_año(2019, calendar.MONDAY)
print(f"\nNúmero de Lunes en 2019: {conteo_lunes}") # Debería ser 52