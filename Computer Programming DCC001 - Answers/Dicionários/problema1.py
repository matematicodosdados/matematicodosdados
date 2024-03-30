from operator import itemgetter
nome = input('')
conta = dict()
nomes = []
lista = []
for i in nome:
    nomes += [i]
for nome in nomes: 
    if nome not in conta: 
        conta[nome] = 1 
    else: 
        conta[nome] = conta[nome] + 1 
tmp = sorted(conta.items(), key=itemgetter(1), reverse=True)
for a,b in tmp: 
    print(a)
    break 
