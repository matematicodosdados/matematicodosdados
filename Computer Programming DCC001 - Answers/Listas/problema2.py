lista = []
for i in range(5):
    i = input()
    lista += [float(i)]
lista.remove(max(lista))
lista.remove(min(lista))
print('Média: %.2f' % (sum(lista)/3))