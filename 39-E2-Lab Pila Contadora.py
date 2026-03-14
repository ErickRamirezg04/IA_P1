# LAB Pila Contadora (Herencia)
# -----------------------------------------------------------------------------
class PilaBase:
    def __init__(self):
        self.__lista_pila = []

    def push(self, valor):
        self.__lista_pila.append(valor)

    def pop(self):
        if len(self.__lista_pila) > 0:
            return self.__lista_pila.pop()
        return None

class PilaContadora(PilaBase):
    def __init__(self):
        super().__init__()
        self.__contador_pops = 0 # Variable privada para contar extracciones

    def get_contador(self):
        return self.__contador_pops

    def pop(self):
        # Sobrescribe el método pop para incrementar el contador cada vez que se llama
        self.__contador_pops += 1
        return super().pop()