numero = int(input('Digite um inteiro: '))
print('Tabuada de %d:'% numero)
for i in range(1,11):
    print(str(numero), 'X', str(i), '= %d'% int(i*numero)) 