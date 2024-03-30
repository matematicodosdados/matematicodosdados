numero = int(input('Digite um número: '))
c = 0 
d = 0 
while numero >= 0:
    b = numero
    if b%2 == 0:
        c += b
    else:
        d += b 
    numero = int(input('Digite um número: '))
print('Soma pares: %d' % c)
print('Soma ímpares: %d' % d)