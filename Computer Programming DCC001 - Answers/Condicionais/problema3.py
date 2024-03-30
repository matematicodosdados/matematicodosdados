idade = int(input('Digite a idade: '))
tempo = int(input('Digite o tempo de contribuição: '))
sexo = input('Digite o sexo (M/F): ')
if sexo == 'M':
    if idade >= 60 and tempo >= 35: 
        print('Pode aposentar')
    elif idade >= 65:
        print('Pode aposentar')
    else:
        print('Não pode aposentar')
if sexo == 'F':
    if idade >= 55 and tempo >= 30: 
        print('Pode aposentar')
    elif idade >= 60:
        print('Pode aposentar')
    else:
        print('Não pode aposentar')