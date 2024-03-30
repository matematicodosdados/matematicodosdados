custo = float(input('Digite o custo de fábrica: '))
if custo <= 12000: 
    print('Custo total: %.2f' % float(custo + custo*0.05))
elif custo > 12000 and custo <= 25000:
    print('Custo total: %.2f' % float(custo + custo*0.1 + custo*0.15))
else: 
    print('Custo total: %.2f' % float(custo + custo*0.15 + custo*0.2))