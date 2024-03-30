dicio = {'UUU': 'Phe', 'CUU': 'Leu', 'UUA': 'Leu', 'AAG': 'Lisina', 'UCU': 'Ser', 'UAU': 'Tyr', 'CAA': 'Gln'}
lista = []
string = ''
nome = input('Digite o RNA: ')
for i in range(int(len(nome)/3)):
    lista += ([dicio[nome[0:3]]])
    nome = nome[3:]
for a in lista:
    string += '-'+str(a)
print('Cadeia de Aminoácidos: %s' % string[1:]) 