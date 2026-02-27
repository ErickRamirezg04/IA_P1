#Operadores Logicos y Operaciones bit a bit
#Operador and: ambas condiciones deben ser true para arrojar un true
#Operador or: ambas deben ser false para arrojar un false
#Operador not: niega su valor

#operadores bit a bit
#& (ampersand) ‒ conjunción a nivel de bits;
#| (barra vertical) - disyunción a nivel de bits;
#~ (tilde) - negación a nivel de bits;
#^ (signo de intercalación) - o exclusivo a nivel de bits (xor).

#xor: Si las entradas son diferentes entonces es true

#desplazamiento binario a la izquierda o a la derecha
#valor << bits
#valor >> bits

var = 53
var_right = var >> 1
var_left = var << 1
print(var, var_left, var_right)

x = 4
y = 1
 
a = x & y
b = x | y
c = ~x  # ¡difícil!
d = x ^ 5
e = x >> 2
f = x << 2
 
print(a, b, c, d, e, f)