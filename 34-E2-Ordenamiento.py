# COMPARACIÓN Y ORDENAMIENTO
# -----------------------------------------------------------------------------

# Comparación basada en valores ASCII.
print('10' == '010') 
print('10' > '010')

# sorted(): Función que devuelve una NUEVA lista con los elementos ordenados.
first_greek = ['omega', 'alpha', 'pi', 'gamma'] 
first_greek_sorted = sorted(first_greek)
print(first_greek)
print(first_greek_sorted) 

# sort(): Método que ordena la lista ORIGINAL (in-place).
second_greek = ['omega', 'alpha', 'pi', 'gamma']
second_greek.sort() 
print(second_greek) 

# Conversión de tipos.
itg_val = 13 
flt_val = 1.3 
str_itg = str(itg_val)
str_flt = str(flt_val) 
print(str_itg + ' ' + str_flt) 

str_si = '13' 
str_sf = '1.3' 
int_val = int(str_si)
float_val = float(str_sf) 
print(int_val + float_val) 