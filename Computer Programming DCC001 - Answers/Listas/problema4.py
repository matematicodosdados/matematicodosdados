lista = []
for i in range(12):
    i = input()
    lista += [int(i)]
print('Média: %.2f' % (sum(lista)/len(lista)))
for j in lista:
    if j > sum(lista)/len(lista):
        print(j)