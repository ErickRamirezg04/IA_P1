# POO: MÉTODOS Y ATRIBUTOS DETALLADOS
# -----------------------------------------------------------------------------

class Robot:
    """Clase para demostrar métodos de instancia, de clase y estáticos."""
    
    poblacion_total = 0  # Atributo de clase (compartido)

    def __init__(self, nombre_robot):
        # Método constructor: Inicializa la instancia
        self.nombre = nombre_robot  # Atributo de instancia
        Robot.poblacion_total += 1
        print(f"Robot {self.nombre} creado.")

    def saludar(self):
        # Método de instancia: Accede a datos del objeto mediante 'self'
        return f"Hola, soy {self.nombre}."

    @classmethod
    def obtener_poblacion(cls):
        # Método de clase: Accede a atributos de la clase mediante 'cls'
        return f"Total de robots: {cls.poblacion_total}"

    @staticmethod
    def es_tecnologia_valida(tipo):
        # Método estático: No accede ni a la clase ni a la instancia
        # Funciona como una función normal dentro del espacio de la clase
        return tipo in ["IA", "Mecánico", "Eléctrico"]

# Pruebas de métodos
obj_bot1 = Robot("R2D2")
print(obj_bot1.saludar())
print(Robot.obtener_poblacion())
print(Robot.es_tecnologia_valida("IA"))