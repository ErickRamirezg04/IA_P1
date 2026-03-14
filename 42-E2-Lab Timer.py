# LAB Timer (Gestión de Tiempo)
# -----------------------------------------------------------------------------
class RelojTemporizador:
    def __init__(self, hh=0, mm=0, ss=0):
        self.__h = hh
        self.__m = mm
        self.__s = ss

    def __str__(self):
        # Formatea el tiempo en HH:MM:SS con ceros a la izquierda
        return f"{str(self.__h).zfill(2)}:{str(self.__m).zfill(2)}:{str(self.__s).zfill(2)}"

    def siguiente_segundo(self):
        self.__s += 1
        if self.__s > 59:
            self.__s = 0
            self.__m += 1
            if self.__m > 59:
                self.__m = 0
                self.__h = (self.__h + 1) % 24

    def anterior_segundo(self):
        self.__s -= 1
        if self.__s < 0:
            self.__s = 59
            self.__m -= 1
            if self.__m < 0:
                self.__m = 59
                self.__h = (self.__h - 1) % 24