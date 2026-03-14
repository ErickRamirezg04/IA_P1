# LAB: TRIÁNGULO (POO Y COMPOSICIÓN)
# -----------------------------------------------------------------------------
import math

class PuntoCoordenada:
    def __init__(self, coord_x=0.0, coord_y=0.0):
        self.__x = coord_x
        self.__y = coord_y

    def obtener_x(self):
        return self.__x

    def obtener_y(self):
        return self.__y

    def distancia_desde_xy(self, destino_x, destino_y):
        # Usa el teorema de Pitágoras para calcular distancia entre puntos 
        return math.hypot(self.__x - destino_x, self.__y - destino_y)

    def distancia_desde_punto(self, otro_punto):
        return self.distancia_desde_xy(otro_punto.obtener_x(), otro_punto.obtener_y())

class TrianguloFigura:
    def __init__(self, v1, v2, v3):
        # El triángulo se compone de tres objetos de la clase PuntoCoordenada 
        self.__vertices = [v1, v2, v3]

    def calcular_perimetro(self):
        suma_lados = 0
        for i in range(3):
            # Calcula la distancia entre el vértice actual y el siguiente (circular) 
            suma_lados += self.__vertices[i].distancia_desde_punto(self.__vertices[(i + 1) % 3])
        return suma_lados

# Ejemplo: tri = TrianguloFigura(PuntoCoordenada(0,0), PuntoCoordenada(1,0), PuntoCoordenada(0,1))