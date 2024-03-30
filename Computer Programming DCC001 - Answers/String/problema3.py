#verificando se é palindromo
nome = input('Digite a string: ')
if nome[:] == nome[::-1]:
    print('É palíndromo')
else:
    print('Não é palíndromo')