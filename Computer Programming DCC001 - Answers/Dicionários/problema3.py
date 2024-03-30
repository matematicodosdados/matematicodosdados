from operator import itemgetter
n1 = 0 
n2 = 0 
n3 = 0 
dicio = dict()
tupla = ()
lista = []
while n1 != '':
    n1 = input('Digite: ')
    if n1 == '':
        break
    tupla = (n1,0,0)
    n2 = input('Digite: ')
    if n2 == '':
        break    
    tupla = (n1,n2,0)
    n3 = input('Digite: ')
    if n3 == '':
        break   
    tupla = (n1,n2,n3)
    lista += [tupla]
for a,b,c in lista:
    dicio[a] = (float(b)+float(c))/2 
tmp = sorted(dicio.items(), key=itemgetter(1), reverse=True)
for a,b in tmp:
    print(a, '- %.2f' % b)
    