from operator import itemgetter
n = 0 
lista = []
dicio = dict()
while n != -1:
    n = int(input(''))
    lista += [n]
for i in lista: 
    if i not in dicio: 
        dicio[i] = 1
    else:
        dicio[i] = dicio[i] + 1
tmp = sorted(dicio.items(), key=itemgetter(1), reverse=True)
for a,b in tmp: 
    print(a)
    break 