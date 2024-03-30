lista = []
lista_impar = []
lista_par = []
for i in range(5):
    i = input()
    lista += [int(i)]
    if int(i)%2 != 0:
        lista_impar += [int(i)]
    else:
        lista_par += [int(i)]
print(lista)
print(lista_par)
print(lista_impar)