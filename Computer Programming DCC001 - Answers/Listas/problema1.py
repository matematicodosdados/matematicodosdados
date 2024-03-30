ip = input()
lista = ip.split('.')
n = 0 
for i in lista: 
    if int(i) > 255 or int(i) < 0: 
        print('Inválido')
        break
    else: 
        n += 1 
if n == 4:
    print('Válido')
    