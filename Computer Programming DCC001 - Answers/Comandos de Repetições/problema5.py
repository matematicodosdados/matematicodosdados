numero = int(input('Digite um inteiro n: '))
a = 0
b = 0 
while a <= numero:
    a = a+1
    if numero%a == 0:
        b += 1 
if b == 1 or b == 2:
    print('É primo')
else:
    print('Não é primo')