# 4. GENERADORES E ITERADORES (CONCEPTOS AVANZADOS)
# -----------------------------------------------------------------------------

# Un Generador es una función que utiliza 'yield' para devolver valores pausadamente
def generador_fibonacci(limite_n):
    n_inicial, n_siguiente = 0, 1
    for _ in range(limite_n):
        yield n_inicial # Pausa la ejecución y devuelve el valor
        n_inicial, n_siguiente = n_siguiente, n_inicial + n_siguiente

# Uso del generador
gen_fib = generador_fibonacci(10)
for num_fibo in gen_fib:
    print(num_fibo, end=" ")
print("\n")

# --- PROTOCOLO DE ITERACIÓN ---
# Un objeto es iterable si implementa __iter__() y __next__()
class ContadorIter:
    def __init__(self, bajo, alto):
        self.actual = bajo
        self.limite = alto

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual > self.limite:
            raise StopIteration # Detiene el bucle
        else:
            self.actual += 1
            return self.actual - 1

obj_iterador = ContadorIter(1, 5)
for n_iter in obj_iterador:
    print(f"Iteración: {n_iter}")