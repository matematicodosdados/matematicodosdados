valor = float(input('Digite o valor do produto: '))
estado = input('Digite o estado: ')
if estado == "MG":
    print('Valor final: %.2f' % float(valor + valor*0.07))
elif estado == "SP":
    print('Valor final: %.2f' % float(valor + valor*0.12))
elif estado == "RJ":
    print('Valor final: %.2f' % float(valor + valor*0.15))
elif estado == "MS":
    print('Valor final: %.2f' % float(valor + valor*0.08))
else:
    print('Estado inválido')
    
    