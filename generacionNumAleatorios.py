import random
import sys

suma = 0
x = 0
sumaS = 0
S = 0
for o in range(100):
    r = random.uniform(10, 20)
    rounded_number = round(r,3)
    suma += rounded_number
    x = suma/100
    sumaS += ( (rounded_number - x)**2)
    #ayuda = rounded_number - x
    #ayuda2 = ayuda**2
    #sumaS += ayuda2
    S = sumaS/(100-1)

    print(str(rounded_number)+'\t', end= ' ')



print('\n\nPromedio\n %2.3f' %(x))
print('\n\nMedia Muestral\n %2.3f' %(S))
