# MÓDULO DATETIME
# -----------------------------------------------------------------------------
# El módulo datetime permite manipular fechas y horas. Proporciona clases como
# date, time, datetime y timedelta[cite: 5].

from datetime import date, time, datetime, timedelta
import time as time_module

# --- Clase date (Fechas) ---
# Representa una fecha (año, mes, día)
hoy = date.today() # Obtiene la fecha actual del sistema 
mi_fecha = date(1992, 1, 16) # Crea una fecha específica 

# --- Clase time (Horas) ---
# Representa una hora independiente del día (hora, minuto, segundo, microsegundo)
hora_evento = time(14, 30, 0) # 14:30:00 

# --- Clase datetime (Fecha y Hora) ---
# Combina información de fecha y hora en un solo objeto
registro_ahora = datetime.now() # Fecha y hora actuales con precisión de microsegundos 
fecha_especifica = datetime(2020, 11, 4, 14, 53, 0) # Definición manual 

# --- Clase timedelta (Duración) ---
# Representa la diferencia entre dos fechas o expresiones de tiempo
lapso_tiempo = timedelta(weeks=2, days=5, hours=3) # Una duración de 19 días y 3 horas 
mañana = hoy + timedelta(days=1) # Operaciones aritméticas con fechas 

# --- Formateo con strftime() ---
# Permite convertir objetos de fecha/hora en cadenas de texto legibles usando directivas
# %Y: Año 4 dígitos, %m: Mes, %d: Día, %H: Hora 24h, %M: Minuto, %S: 
print(fecha_especifica.strftime("%Y/%m/%d %H:%M:%S")) # Formato ISO básico 