nome = input('Digite o nome: ')
a = ' '
b = nome.rfind(a)
print('Nome formatado: %s' % nome[b+1:] + ',',nome[:b])