dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))
if ano%4 == 0 or ano%400 == 0 and dia >= 1 and dia <= 31 and mes >= 1 and mes <= 12: 
    if mes == 2 and dia >= 1 and dia <= 29:
        print('Data válida')
    elif mes == 4 and dia > 30 or mes == 6 and dia > 30 or mes == 9 and dia > 30 or mes == 11 and dia > 30:
        print('Data inválida')
    elif dia >= 1 and dia <= 31 and mes != 2:
        print('Data válida')
    else:
        print('Data inválida')
elif dia >= 1 and dia <= 31 and mes >= 1 and mes <= 12:
    if mes == 2 and dia > 28: 
        print('Data inválida')
    elif mes == 4 and dia > 30 or mes == 6 and dia > 30 or mes == 9 and dia > 30 or mes == 11 and dia > 30:
        print('Data inválida')
    else:
        print('Data válida')       
else:
    print('Data inválida')

        
    
    
