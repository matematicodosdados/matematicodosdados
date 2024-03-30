palavra = input('Digite uma palavra: ')
chave = int(input('Digite o valor da chave: '))
palavranova = ''
for i in palavra: 
    palavranova += chr(ord(i) + chave%26)
print('Resultado: ',palavranova)