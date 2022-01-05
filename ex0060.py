import math
from time import sleep
print('Calculo de fatorial')
n = int(input('Digite um numero:'))
c=n
print('Calculando o fatorial de {}!'.format(n))
sleep(1)
while c > 0:
    print('{} x '.format(c), end='')
    c -= 1
print(' = {}'.format(math.factorial(n)))
