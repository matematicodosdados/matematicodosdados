nome1 = input('Coloque a droga do nome: ')
for i in nome1:
    if i+i in nome1: 
        a = i
        a_upper = a.upper()
        nome1 = nome1.replace(i+i, a_upper)
print(nome1)