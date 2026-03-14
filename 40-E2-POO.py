# PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
# -----------------------------------------------------------------------------

# Clase básica (The SimplestClass)
class TheSimplestClass:
    pass

# Implementación de una Pila (Stack) usando listas.
stack_list = [] 
def push_val(val):
    stack_list.append(val) 

def pop_val(): 
    val = stack_list[-1]
    del stack_list[-1] 
    return val 

# Implementación de Pila usando Clases.
class Stack: 
    def __init__(self): 
        self.__stack_list = [] 

    def push(self, val): 
        self.__stack_list.append(val) 

    def pop(self):
        val = self.__stack_list[-1] 
        del self.__stack_list[-1] 
        return val

# Herencia: Una clase que extiende a Stack agregando funcionalidad de suma.
class AddingStack(Stack):
    def __init__(self): 
        Stack.__init__(self)
        self.__sum = 0 

    def get_sum(self): 
        return self.__sum 

    def push(self, val): 
        self.__sum += val 
        Stack.push(self, val) 

    def pop(self): 
        val = Stack.pop(self) 
        self.__sum -= val # Se resta el valor al sacarlo de la pila
        return val 

# Variables de Clase vs Instancia.
class CounterClass:
    counter = 0 # Variable de clase: compartida por todas las instancias [cite: 287]
    def __init__(self, val=1):
        self.first = val # Variable de instancia [cite: 288]
        CounterClass.counter += 1 

# hasattr(): Comprueba si una clase o instancia tiene un atributo específico.
print(hasattr(CounterClass, 'counter')) 