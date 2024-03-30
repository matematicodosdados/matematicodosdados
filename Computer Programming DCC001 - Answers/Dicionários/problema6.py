unidades = {'0': '', '1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V', '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX'}
dezenas = {'0': '', '1': 'X', '2': 'XX', '3': 'XXX', '4': 'XL', '5': 'L', '6': 'LX', '7': 'LXX', '8': 'LXXX', '9': 'XC'}
centenas = {'0': '', '1': 'C', '2': 'CC', '3': 'CCC', '4': 'CD', '5': 'D', '6': 'DC', '7': 'DCC', '8': 'DCCC', '9': 'CM'}
numero = input('Digite um número: ')
lista = []
for i in range(len(numero)-1, -1, -1):
    lista += [numero[i]]
if len(lista) == 1:
    print('Número Romano: ',unidades[lista[0]])
if len(lista) == 2: 
    print('Número Romano: ',dezenas[lista[1]] + unidades[lista[0]])
if len(lista) == 3:
    print('Número Romano: ',centenas[lista[2]] + dezenas[lista[1]] + unidades[lista[0]])