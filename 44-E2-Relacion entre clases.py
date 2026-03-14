# HERENCIA (SIMPLE Y MÚLTIPLE) Y RELACIÓN ENTRE CLASES
# -----------------------------------------------------------------------------

class Vehiculo:
    """Superclase Base"""
    def __init__(self, marca):
        self.marca = marca

    def encender(self):
        return f"{self.marca} está encendido."

class Terrestre(Vehiculo):
    """Herencia Simple: Terrestre hereda de Vehiculo"""
    def conducir(self):
        return "Conduciendo por carretera."

class Volador(Vehiculo):
    """Superclase para drones/aviones"""
    def volar(self):
        return "Volando por el aire."

# Herencia Múltiple: La clase Drone hereda de Terrestre y Volador
class Drone(Terrestre, Volador):
    def __init__(self, marca, modelo):
        # super() ayuda a llamar métodos de las clases padre
        super().__init__(marca)
        self.modelo = modelo

# MRO (Method Resolution Order): El orden en que Python busca métodos
# Se puede consultar con el atributo __mro__
print(f"Orden de resolución de Drone: {Drone.__mro__}")

# --- RELACIÓN ENTRE CLASES: COMPOSICIÓN ---
class Motor:
    def __init__(self, caballos):
        self.caballos = caballos

class Auto:
    def __init__(self, marca, caballos):
        # Composición: El Auto "TIENE UN" Motor (el motor vive dentro del auto)
        self.mi_motor = Motor(caballos)
        self.marca = marca