salario = float(input('Digite o valor do salário: '))
if salario <= 280: 
    print('Valor do aumento: %.2f' % float(salario*0.2))
    print('Novo salário: %.2f' % float(salario + salario*0.2))
elif salario > 280 and salario <= 700:
    print('Valor do aumento: %.2f' % float(salario*0.15))
    print('Novo salário: %.2f' % float(salario + salario*0.15))
elif salario > 700 and salario <= 1500:
    print('Valor do aumento: %.2f' % float(salario*0.1))
    print('Novo salário: %.2f' % float(salario + salario*0.1))
else:
    print('Valor do aumento: %.2f' % float(salario*0.05))
    print('Novo salário: %.2f' % float(salario + salario*0.05))
    